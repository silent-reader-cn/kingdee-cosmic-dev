# 产品经理产品设置-occbo_productset

## 产品经理产品设置-主表 t_occbo_productset

- **表名称：** 产品经理产品设置-主表
- **表名：** t_occbo_productset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemclassid | 产品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 3 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 4 | fuserid | 产品经理 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fitemid | 产品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_productset_uiic |  | fuserid,fitemid,fitemclassid |
| 2 | pk_occbo_productset |  | fid |
