# 商品映射（弃用）-bdm_goods_mapping

## 商品映射（弃用）-主表 t_bdm_goods_mapping

- **表名称：** 商品映射（弃用）-主表
- **表名：** t_bdm_goods_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconversationrate | 单位换算率 | varchar | 50 |  | √ | ' ' | 单位换算率 |
| 3 | foriginalgoodsspecial | 原规格型号 | varchar | 40 |  | √ | ' ' | 原规格型号 |
| 4 | feffectbuyerids | 生效购方(ID) | varchar | 1000 |  | √ | ' ' | 生效购方(ID) |
| 5 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | feffectbuyers | 指定生效名称 | varchar | 1000 |  | √ | ' ' | 指定生效名称 |
| 7 | foriginalgoodsname | 原商品名称 | varchar | 92 |  | √ | ' ' | 原商品名称 |
| 8 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | feffectivescope | 生效范围 | varchar | 50 |  | √ | ' ' | 生效范围,枚举: 2 :全部购方 1 :指定购方 |
| 11 | foriginalgoodsunit | 原计量单位 | varchar | 14 |  | √ | ' ' | 原计量单位 |
| 12 | fenjoyprivileges | 优惠政策类型 | varchar | 50 |  | √ | ' ' | 优惠政策类型,枚举: 1 :享受 0 :不享受 |
| 13 | fsysgoodsname | 商品名称 | int8 | 64 |  | √ | 0 | 开票项管理 bdm_goods_info |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_goods_mapping |  | fid |
| 2 | idx_bdm_goods_mapping |  | forg |
