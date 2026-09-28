# 导入结果-gl_import_report

## 导入结果-主表 t_gl_importreport

- **表名称：** 导入结果-主表
- **表名：** t_gl_importreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffailedcount | 失败 | int8 | 64 |  | √ | 0 | 失败 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 6 | fentitykey | 导入对象内码 | varchar | 36 |  | √ | ' ' | 导入对象内码 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fdetail_tag | 明细信息_详情 | text | 0 |  |  | null | 明细信息_详情 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fentityname | 导入对象 | varchar | 60 |  | √ | ' ' | 导入对象 |
| 11 | fstatus | 导入状态 | bpchar | 1 |  | √ | ' ' | 导入状态,枚举: 0 :导入中 1 :异常 2 :完成 |
| 12 | fdetail | 明细信息 | varchar | 255 |  | √ | ' ' | 明细信息 |
| 13 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbookname | 账簿 | varchar | 255 |  | √ | ' ' | 账簿 |
| 15 | fmainorgname | 主业务组织 | varchar | 255 |  | √ | ' ' | 主业务组织 |
| 16 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 17 | ftotalcount | 总数 | int8 | 64 |  | √ | 0 | 总数 |
| 18 | fusetime | 用时 | varchar | 50 |  | √ | ' ' | 用时 |
| 19 | fbillno | 编号 | varchar | 100 |  | √ | ' ' | 编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fsuccesscount | 成功 | int8 | 64 |  | √ | 0 | 成功 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_importreport_ekey |  | fentitykey |
| 2 | pk_gl_importreport |  | fid |
