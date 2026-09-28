# 用户许可分组试算-lic_userlicgroup_trial

## 用户许可分组试算-主表 t_lic_userlicgroup_trial

- **表名称：** 用户许可分组试算-主表
- **表名：** t_lic_userlicgroup_trial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmainorgfullname | 主职部门长名称 | varchar | 255 |  | √ | ' ' | 主职部门长名称 |
| 3 | fgroupid | 许可分组 | int8 | 64 |  | √ | 0 | 许可分组 lic_group |
| 4 | fstatus | 使用状态 | varchar | 30 |  | √ | '1' | 使用状态,枚举: 1 :可用 0 :不可用 |
| 5 | forgid | 组织机构 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | flicensesource | 许可来源 | varchar | 10 |  | √ | ' ' | 许可来源,枚举: 1 :授权分配 2 :手动分配 3 :用户平台分配 4 :接口分配 5 :自动分配 6 :重新分配 0 :其它 |
| 7 | fmainorgname | 主职部门 | varchar | 255 |  | √ | ' ' | 主职部门 |
| 8 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fsynclogid | 同步日志 | int8 | 64 |  | √ | 0 | 同步日志 |
| 10 | fsyncstatus | 同步状态 | varchar | 30 |  | √ | ' ' | 同步状态,枚举: 2 :未同步 1 :已同步 3 :同步异常 4 :已释放 |
| 11 | fassigntime | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lic_userlicgroup_trial_ug |  | fuserid,fgroupid |
| 2 | pk_t_lic_userlicgroup_trial |  | fid |
