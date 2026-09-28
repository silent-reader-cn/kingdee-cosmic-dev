# 代扣代缴税收通用缴款书抵扣清单-tcvat_ybnsr_dkdjdkqd

## 代扣代缴税收通用缴款书抵扣清单-主表 t_tcvat_ybnsr_dkdjdkqd

- **表名称：** 代扣代缴税收通用缴款书抵扣清单-主表
- **表名：** t_tcvat_ybnsr_dkdjdkqd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdkdjpzbh | 代扣代缴凭证编号 | varchar | 50 |  | √ | ' ' | 代扣代缴凭证编号 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 sum :合计 |
| 4 | fkqrsbh | 扣缴人纳税人识别号 | varchar | 50 |  | √ | ' ' | 扣缴人纳税人识别号 |
| 5 | fzsjgmc | 征收机关名称 | varchar | 200 |  | √ | ' ' | 征收机关名称 |
| 6 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 7 | ftaxmoney | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 8 | fkqrmc | 扣缴人名称 | varchar | 200 |  | √ | ' ' | 扣缴人名称 |
| 9 | fdkdjxm | 代扣代缴项目 | varchar | 200 |  | √ | ' ' | 代扣代缴项目 |
| 10 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_ybnsr_dkdjdkqd_1 |  | fsbbid,fewblname,fewblxh |
| 2 | pk_tcvat_ybnsr_dkdjdkqd |  | fid |
