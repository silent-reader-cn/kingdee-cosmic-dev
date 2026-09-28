# 批号入库跟踪记录-im_lotintrack

## 批号入库跟踪记录-主表 t_im_lotintrack

- **表名称：** 批号入库跟踪记录-主表
- **表名：** t_im_lotintrack

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 9 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 10 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_lottrack_flotnumber |  | flotnumber |
| 2 | idx_im_lottrack_unq |  | forgid,fmaterialid,flotnumber,fproducedate,fexpirydate |
| 3 | idx_im_lottrack_material |  | fmaterialid |
| 4 | t_im_lotintrack_pkey |  | fid |
