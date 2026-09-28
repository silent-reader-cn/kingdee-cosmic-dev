# 用户工作时段-ssc_userworkperiod

## 用户工作时段-主表 t_tk_userworkperiod

- **表名称：** 用户工作时段-主表
- **表名：** t_tk_userworkperiod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fusergroup | 用户组 | int8 | 64 |  | √ | 0 | 用户组 |
| 4 | fuser | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmonthofyear | 月份 | int8 | 64 |  | √ | 0 | 月份 |
| 6 | fmonthlyworkperiod_tag | 每月工作时段_详情 | text | 0 |  |  | null | 每月工作时段_详情 |
| 7 | fmonthlyworkperiod | 每月工作时段 | varchar | 255 |  | √ | ' ' | 每月工作时段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_userworkperiod |  | fid |
| 2 | idx_ssc_userworkperiod_union |  | fsscid,fusergroup,fuser,fmonthofyear |
