# 共享人员在岗时长统计表-ssc_userondutytime

## 共享人员在岗时长统计表-主表 t_tk_sscuserondutytime

- **表名称：** 共享人员在岗时长统计表-主表
- **表名：** t_tk_sscuserondutytime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fgroupid | 用户组 | int8 | 64 |  | √ | 0 | 用户组 task_usergroup |
| 4 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: 1 :有效 2 :无效 |
| 5 | fdutytimebitset | 在岗时长分钟位图 | varchar | 1500 |  | √ | ' ' | 在岗时长分钟位图 |
| 6 | fdatesource | 数据来源 | bpchar | 1 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :手工导入 |
| 7 | fiswork | 是否工作日 | bpchar | 1 |  | √ | '1' | 是否工作日,枚举: 1 :是 2 :否 |
| 8 | fdaten | 日期 | timestamp | 0 |  |  | null | 日期 |
| 9 | fondutytime | 在岗时长 | numeric | 23 | 10 | √ | 0 | 在岗时长 |
| 10 | fleavetime | 请假时长 | numeric | 23 | 10 | √ | 0 | 请假时长 |
| 11 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fovertime | 加班时长 | numeric | 23 | 10 | √ | 0 | 加班时长 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_userondutytime_union1 |  | fsscid,fdaten,fgroupid,fuserid |
| 2 | pk_t_tk_sscuserondutytime |  | fid |
