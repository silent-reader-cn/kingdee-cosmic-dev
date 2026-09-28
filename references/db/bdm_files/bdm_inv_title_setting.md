# 开票抬头设置-bdm_inv_title_setting

## 开票抬头设置-主表 t_bdm_inv_title_setting

- **表名称：** 开票抬头设置-主表
- **表名：** t_bdm_inv_title_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitmappinvbatch | 批量开票 | bpchar | 1 |  | √ | '0' | 批量开票 |
| 3 | fsplitmergeinvoice | 单据拆合 | bpchar | 1 |  | √ | '0' | 单据拆合 |
| 4 | fiscomplete | 数据补全 | bpchar | 1 |  | √ | '0' | 数据补全 |
| 5 | fsingleinvoice | 单张开票 | bpchar | 1 |  | √ | '0' | 单张开票 |
| 6 | ftitmappinvapi | API开票 | bpchar | 1 |  | √ | '0' | API开票 |
| 7 | fautosavetitle | 是否自动保存企业抬头信息 | bpchar | 1 |  | √ | '0' | 是否自动保存企业抬头信息 |
| 8 | fapiinvoice | 接口同步 | bpchar | 1 |  | √ | '0' | 接口同步 |
| 9 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fbatchinvoice | 批量开票 | bpchar | 1 |  | √ | '0' | 批量开票 |
| 11 | fscaninvoice | 扫码开票 | bpchar | 1 |  | √ | '0' | 扫码开票 |
| 12 | ftitmappbillimport | 原始单据导入 | bpchar | 1 |  | √ | '0' | 原始单据导入 |
| 13 | ftitmappbillpush | 原始单据接口 | bpchar | 1 |  | √ | '0' | 原始单据接口 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_inv_title_setting |  | fid |
| 2 | idx_bdm_inv_title_setting |  | forg |
