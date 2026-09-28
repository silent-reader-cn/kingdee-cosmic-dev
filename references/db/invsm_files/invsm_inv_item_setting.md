# 开票项设置-invsm_inv_item_setting

## 开票项设置-主表 t_invsm_inv_item_setting

- **表名称：** 开票项设置-主表
- **表名：** t_invsm_inv_item_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facceptuplevelshare | 接收上级共享商品 | bpchar | 1 |  | √ | ' ' | 接收上级共享商品 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fbatchinvoice | 批量开票 | bpchar | 1 |  | √ | ' ' | 批量开票 |
| 6 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | foriginalbillimport | 原始单据导入 | bpchar | 1 |  | √ | ' ' | 原始单据导入 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fapiinvoice | API开票 | bpchar | 1 |  | √ | ' ' | API开票 |
| 10 | forginalbillnew | 原始单据API新增 | bpchar | 1 |  | √ | ' ' | 原始单据API新增 |
| 11 | forg | 组织 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invsm_inv_item_setting |  | fid |
| 2 | idx_invsm_inv_item_setting |  | forg |
