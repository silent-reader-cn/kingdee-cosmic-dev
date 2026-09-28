# 额外加减分-ssc_extrapoints

## 额外加减分-主表 t_tk_extrapoints

- **表名称：** 额外加减分-主表
- **表名：** t_tk_extrapoints

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 4 | fuserid | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fproject | 加减分项目 | int8 | 64 |  | √ | 0 | [绩效指标 ssc_achievetarget](../som_files/ssc_achievetarget.md) |
| 6 | freason | 加减分原因 | varchar | 1000 |  | √ | ' ' | 加减分原因 |
| 7 | fscore | 加减分值 | numeric | 19 | 6 | √ | 0 | 加减分值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_extrapoints |  | fid |
| 2 | idx_ssc_extrapoints_id |  | fsscid,fuserid,fdate |
