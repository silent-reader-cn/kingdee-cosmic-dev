# 未登账凭证-cas_glvouchernotbook

## 未登账凭证-主表 t_cas_glvouchernotbook

- **表名称：** 未登账凭证-主表
- **表名：** t_cas_glvouchernotbook

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftypeid | 凭证类型 | int8 | 64 |  | √ | 0 | 凭证字 gl_vouchertype |
| 3 | fvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 4 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 5 | fsourcetype | 来源类型 | varchar | 2 |  | √ | ' ' | 来源类型,枚举: 0 :手工凭证 1 :结转损益 2 :期末调汇 3 :模式凭证 4 :机制凭证 5 :凭证摊销 6 :自动转账 7 :扫描生成 8 :外部导入 a :账簿协同 b :凭证对照 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fisall | 是否部分登账 | bpchar | 1 |  | √ | '0' | 是否部分登账 |
| 8 | fbillno | 凭证号 | varchar | 250 |  | √ | ' ' | 凭证号 |
| 9 | fischeck | 复核状态 | bpchar | 1 |  | √ | '0' | 复核状态,枚举: b :待复核 c :已复核 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_glvouchernotbook |  | fid |
| 2 | idx_cas_vb_ischeck_date |  | fbookeddate,fischeck |
| 3 | idx_cas_vb_billno |  | fbillno |
