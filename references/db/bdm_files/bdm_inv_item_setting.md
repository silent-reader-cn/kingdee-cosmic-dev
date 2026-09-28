# 开票项设置-bdm_inv_item_setting

## 开票项设置-主表 t_bdm_inv_item_setting

- **表名称：** 开票项设置-主表
- **表名：** t_bdm_inv_item_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facceptuplevelshare | 接收上级共享商品 | bpchar | 1 |  | √ | ' ' | 接收上级共享商品 |
| 3 | foriginalbillimport | 原始单据导入 | bpchar | 1 |  | √ | ' ' | 原始单据导入 |
| 4 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fapiinvoice | API开票 | bpchar | 1 |  | √ | ' ' | API开票 |
| 6 | forginalbillnew | 原始单据API新增 | bpchar | 1 |  | √ | ' ' | 原始单据API新增 |
| 7 | fsavefrombill | 开票申请单保存 | bpchar | 1 |  | √ | '0' | 开票申请单保存 |
| 8 | forg | 组织 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |
| 9 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fbatchinvoice | 批量开票 | bpchar | 1 |  | √ | ' ' | 批量开票 |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcompletion | 自动补全 | bpchar | 1 |  | √ | '0' | 自动补全 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_inv_item_setting |  | fid |
| 2 | idx_bdm_inv_item_setting |  | forg |
