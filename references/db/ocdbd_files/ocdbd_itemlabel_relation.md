# 商品标签关联商品-ocdbd_itemlabel_relation

## 商品标签关联商品-主表 t_ocdbd_item_labelentry

- **表名称：** 商品标签关联商品-主表
- **表名：** t_ocdbd_item_labelentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 商品标签 | int8 | 64 |  | √ | 0 | [商品标签 ocdbd_item_label](../ocdbd_files/ocdbd_item_label.md) |
| 2 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | forder | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_ilentry_fid |  | fid |
| 2 | idx_ocdbd_ilentry_item |  | fitemid,fmaterielid |
| 3 | pk_ocdbd_item_labelentry |  | fentryid |
