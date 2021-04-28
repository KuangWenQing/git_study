#-----this file introduces the command of the git


git init		    # initialise repository
git add	fileName	    # add file to index
git commit -m '版本说明'    # commit to repository

git status
git diff
git log                     # print version information (barring reset operate
git log --pretty=oneline    # print oneline version info
git reflog		    # print all version info (includ reset operate

#---------------------------------------#
# very important, Like regret medicine  #
#---------------------------------------#
git checkout -- fileName.txt    # before 'git add', 
                                # you can use this command to undo changes

                                # after 'git add', 
git reset HEAD fileName.txt     # you should first execute this command, and then
                                # you can use the previous command (git checkout --)

git reset --hard HEAD^		# Back to previous 			version
git reset --hard HEAD^^		# Back to previous previous 		version
git reset --hard HEAD^^^	# Back to previous previous previous 	version
				# ......
git reset --hard HEAD~100	# Back to the top 100 			version

git reset --hard 123456		# Back to the version which the first 6
				# digits of version number are 123456

# git mv 和 git rm 相对于 linux 的 mv 和 rm, 自动完成了 git add 
git mv file1 file2
git rm file			
git commit -m 'delete file'	# You can 'commit' directly

git commit --amend              # 修改最新提交的 注释
git rebase -i HEAD~2            # 修改倒数第2 次提交的注释

#---------------------------------------------------#
# push your repository to the remote github server  #
#---------------------------------------------------#
git remote add origin git@github.com:KuangWenQing/learnGit.git
git push -u origin master


#---------------------------#
# clone from github server  # 
#        2 methods          #
#---------------------------#
git clone git@github.com:michaelliao/gitskills.git
git clone https://github.com/michaelliao/gitskills.git



git branch dev          # create a branch named dev; 
git checkout dev        # switch to the dev.
git checkout -b dev     # Equivalent to the 2 statements above

git branch              # View current branch
git checkout master     # switch to the master
git merge dev           # merge dev to the master
git branch -d dev       # delete the branch named dev

git switch -c featurel  # create a branch named dev and switch to the featurel
git switch master       # switch to the master
git merge --no-ff -m "merge with no-ff" dev
