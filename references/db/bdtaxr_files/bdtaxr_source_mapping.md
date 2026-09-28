# 税源与申报表映射关系表-bdtaxr_source_mapping

## 税源与申报表映射关系表-主表 t_bdtaxr_source_mapping

- **表名称：** 税源与申报表映射关系表-主表
- **表名：** t_bdtaxr_source_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 申报表ID |
| 3 | ftaxsourcetype | 税源类型 | varchar | 50 |  | √ | ' ' | 税源类型,枚举: tdm_tdzzs_clearing_unit :土地增值税项目 |
| 4 | ftaxsourceid | 税源ID | int8 | 64 |  | √ | 0 | 土地增值税项目 tdm_tdzzs_clearing_unit |
| 5 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: yhsaq :印花税（按期） yhsac :印花税（按次） fcscj :房产税（从价） fcscz :房产税（从租） cztdsys :城镇土地使用税 hbsaq :环保税（按期） ccscl :车船税（车辆） ccscb :车船税（船舶） qs :契税 tdzzs :土地增值税（尾盘） tdzzsyj :土地增值税（预征） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_sm_sbbid |  | fsbbid |
| 2 | pk_bdtaxr_source_mapping |  | fid |
