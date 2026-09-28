# 定制引入报告-gl_iptm_importreport

## 定制引入报告-主表 t_iptm_importreport

- **表名称：** 定制引入报告-主表
- **表名：** t_iptm_importreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ffailedcount | 失败 | int8 | 64 |  | √ | 0 | 失败 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 6 | fentitykey | 引入对象内码 | varchar | 36 |  | √ | ' ' | 引入对象内码 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fdetail_tag | 明细信息_详情 | text | 0 |  |  | null | 明细信息_详情 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fentityname | 引入对象 | varchar | 60 |  | √ | ' ' | 引入对象 |
| 12 | fstatus | 引入状态 | bpchar | 1 |  | √ | ' ' | 引入状态,枚举: 0 :引入中 1 :异常 2 :完成 |
| 13 | fdetail | 明细信息 | varchar | 255 |  | √ | ' ' | 明细信息 |
| 14 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmainorgname | 主业务组织 | varchar | 255 |  | √ | ' ' | 主业务组织 |
| 16 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 17 | ftotalcount | 总数 | int8 | 64 |  | √ | 0 | 总数 |
| 18 | fusetime | 用时 | varchar | 20 |  | √ | ' ' | 用时 |
| 19 | fbillno | 编号 | varchar | 100 |  | √ | ' ' | 编号 |
| 20 | fsuccesscount | 成功 | int8 | 64 |  | √ | 0 | 成功 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_importreport |  | fid |
| 2 | idx_iptm_imptrpt_entitykey |  | fentitykey |
| 3 | idx_iptm_imptrpt_orgname |  | fmainorgname |
