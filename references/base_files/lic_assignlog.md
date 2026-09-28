# 许可分配日志-lic_assignlog

## 许可分配日志-主表 t_lic_assignlog

- **表名称：** 许可分配日志-主表
- **表名：** t_lic_assignlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperate | 操作 | varchar | 30 |  | √ | ' ' | 操作,枚举: 0 :新增 1 :删除 |
| 3 | fgroupid | 许可分组 | int8 | 64 |  | √ | 0 | 许可分组 lic_group |
| 4 | fstatus | 分配状态 | varchar | 30 |  | √ | ' ' | 分配状态 |
| 5 | foptime | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 6 | foperatetype | 分配来源 | varchar | 30 |  | √ | '1' | 分配来源,枚举: 1 :授权分配 2 :手动分配 3 :用户平台分配 4 :接口分配 5 :自动分配 6 :重新分配 0 :其它 |
| 7 | fopuserid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fassignuserid | 分配用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_lic_assignlog_assignuserid |  | fassignuserid |
| 2 | pk_t_lic_assignlog |  | fid |
