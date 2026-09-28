# ippm 模块表清单

> 本模块共收录 **45** 张表定义，来自 `ippm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ippm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ippm_assignrole` | 角色-多选基础资料表 | 4 | [ippm_courseassign.md](./ippm_courseassign.md) |
| 2 | `t_ippm_assigntrainee` | 学员-多选基础资料表 | 3 | [ippm_courseassign.md](./ippm_courseassign.md) |
| 3 | `t_ippm_baseparam` | 基础参数-主表 | 4 | [ippm_baseparam.md](./ippm_baseparam.md) |
| 4 | `t_ippm_catalog` | 实施文档-主表 | 13 | [ippm_catalog.md](./ippm_catalog.md) |
| 5 | `t_ippm_catalog_l` | 实施文档-多语言表 | 4 | [ippm_catalog.md](./ippm_catalog.md) |
| 6 | `t_ippm_categorygroup` | 文件夹-主表 | 12 | [ippm_categorygroup.md](./ippm_categorygroup.md) |
| 7 | `t_ippm_categorygroup_l` | 文件夹-多语言表 | 5 | [ippm_categorygroup.md](./ippm_categorygroup.md) |
| 8 | `t_ippm_course` | 课程-主表 | 10 | [ippm_course.md](./ippm_course.md) |
| 9 | `t_ippm_courseassign` | 课程分配-主表 | 7 | [ippm_courseassign.md](./ippm_courseassign.md) |
| 10 | `t_ippm_courselist` | 课程清单-主表 | 8 | [ippm_courselist.md](./ippm_courselist.md) |
| 11 | `t_ippm_impldoc_file` | 附件-附件表 | 3 | [ippm_catalog.md](./ippm_catalog.md) |
| 12 | `t_ippm_impldoc_log` | 实施文档操作记录-主表 | 12 | [ippm_impldoc_log.md](./ippm_impldoc_log.md) |
| 13 | `t_ippm_impldoc_log` | 实施文档操作日志-主表 | 12 | [t_ippm_impldoc_logs.md](./t_ippm_impldoc_logs.md) |
| 14 | `t_ippm_impldoc_log_l` | 实施文档操作记录-多语言表 | 4 | [ippm_impldoc_log.md](./ippm_impldoc_log.md) |
| 15 | `t_ippm_impldoc_log_l` | 实施文档操作日志-多语言表 | 4 | [t_ippm_impldoc_logs.md](./t_ippm_impldoc_logs.md) |
| 16 | `t_ippm_learningdetail` | 学习明细-主表 | 6 | [ippm_learningdetail.md](./ippm_learningdetail.md) |
| 17 | `t_ippm_learningrecord` | 学习进度-主表 | 10 | [ippm_learningrecord.md](./ippm_learningrecord.md) |
| 18 | `t_ippm_learnrecordtime` | 学习记录调用时间-主表 | 5 | [ippm_learnrecordtime.md](./ippm_learnrecordtime.md) |
| 19 | `t_ippm_otheraccountuser` | 其他数据中心用户-主表 | 3 | [ippm_otheraccountuser.md](./ippm_otheraccountuser.md) |
| 20 | `t_ippm_paperdetail` | 答卷明细-主表 | 6 | [ippm_paperdetail.md](./ippm_paperdetail.md) |
| 21 | `t_ippm_paramchange` | 参数变动监控-主表 | 14 | [ippm_paramchange.md](./ippm_paramchange.md) |
| 22 | `t_ippm_paramconfig` | 报告参数配置-主表 | 10 | [ippm_paramconfig.md](./ippm_paramconfig.md) |
| 23 | `t_ippm_paramdatasource` | 报告参数数据源-主表 | 12 | [ippm_paramdatasource.md](./ippm_paramdatasource.md) |
| 24 | `t_ippm_paramfieldentry` | 数据字段单据体-子表 | 7 | [ippm_paramdatasource.md](./ippm_paramdatasource.md) |
| 25 | `t_ippm_paramrefentry` | 关联属性单据体-子表 | 5 | [ippm_paramdatasource.md](./ippm_paramdatasource.md) |
| 26 | `t_ippm_paramstorage` | 参数数据存储-主表 | 5 | [ippm_paramstorage.md](./ippm_paramstorage.md) |
| 27 | `t_ippm_problem_knownuser` | 首页问题反馈与建议不提示人员-主表 | 4 | [ippm_problem_knownuser.md](./ippm_problem_knownuser.md) |
| 28 | `t_ippm_problemcusfield` | 项目问题扩展字段-主表 | 10 | [ippm_problemcusfield.md](./ippm_problemcusfield.md) |
| 29 | `t_ippm_problemcusfield_l` | 项目问题扩展字段-多语言表 | 4 | [ippm_problemcusfield.md](./ippm_problemcusfield.md) |
| 30 | `t_ippm_problemlist` | 项目问题列表-主表 | 49 | [ippm_problemlist.md](./ippm_problemlist.md) |
| 31 | `t_ippm_problemlist` | 反馈问题-主表 | 49 | [ippm_problemlist_home.md](./ippm_problemlist_home.md) |
| 32 | `t_ippm_problemlist` | 反馈建议-主表 | 49 | [ippm_suggest_home.md](./ippm_suggest_home.md) |
| 33 | `t_ippm_problemlist` | AI记账申请记录-主表 | 49 | [tc_aiaccapplyrecord.md](./tc_aiaccapplyrecord.md) |
| 34 | `t_ippm_problemlist_entity` | 单据体-子表 | 9 | [ippm_problemlist.md](./ippm_problemlist.md) |
| 35 | `t_ippm_problemlist_entity` | 单据体-子表 | 9 | [ippm_problemlist_home.md](./ippm_problemlist_home.md) |
| 36 | `t_ippm_problemlist_entity` | 单据体-子表 | 9 | [ippm_suggest_home.md](./ippm_suggest_home.md) |
| 37 | `t_ippm_problemlist_entity` | 单据体-子表 | 9 | [tc_aiaccapplyrecord.md](./tc_aiaccapplyrecord.md) |
| 38 | `t_ippm_problemlist_log` | 单据体-子表 | 6 | [ippm_problemlist.md](./ippm_problemlist.md) |
| 39 | `t_ippm_problemlist_log` | 单据体-子表 | 6 | [ippm_problemlist_home.md](./ippm_problemlist_home.md) |
| 40 | `t_ippm_problemlist_log` | 单据体-子表 | 6 | [ippm_suggest_home.md](./ippm_suggest_home.md) |
| 41 | `t_ippm_problemlist_log` | 单据体-子表 | 6 | [tc_aiaccapplyrecord.md](./tc_aiaccapplyrecord.md) |
| 42 | `t_ippm_quizdetail` | 考试明细-主表 | 4 | [ippm_quizdetail.md](./ippm_quizdetail.md) |
| 43 | `t_ippm_replyunreadstatus` | 反馈与建议回复未读状态-主表 | 3 | [ippm_replyunreadstatus.md](./ippm_replyunreadstatus.md) |
| 44 | `t_ippm_savedtenement` | 租户是否已保存-主表 | 4 | [ippm_savedtenement.md](./ippm_savedtenement.md) |
| 45 | `t_ippm_trainconfig` | 培训配置-主表 | 4 | [ippm_trainconfig.md](./ippm_trainconfig.md) |
