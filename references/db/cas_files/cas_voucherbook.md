# 凭证登账异常-cas_voucherbook

## 凭证登账异常-主表 t_cas_voucherbook

- **表名称：** 凭证登账异常-主表
- **表名：** t_cas_voucherbook

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrormsg | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fsourcebillid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 5 | ferrortype | 异常类别 | varchar | 50 |  | √ | ' ' | 异常类别,枚举: KD :业务异常 EX :系统异常 |
| 6 | fbusinesstype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: BOOK :登账 CANCELBOOK :取消登账 |
| 7 | ferrormsg_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_voucherbook_sid |  | fsourcebillid |
| 2 | pk_t_cas_voucherbook |  | fid |
