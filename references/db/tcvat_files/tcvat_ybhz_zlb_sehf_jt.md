# 一般汇总总览表税额划分_计提-tcvat_ybhz_zlb_sehf_jt

## 一般汇总总览表税额划分_计提-主表 t_tcvat_ybhz_zlb_sehf_jt

- **表名称：** 一般汇总总览表税额划分_计提-主表
- **表名：** t_tcvat_ybhz_zlb_sehf_jt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 销项税额 | numeric | 23 | 10 | √ | 0 | 销项税额 |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsuborgname | fsuborgname | varchar | 50 |  | √ | ' ' |  |
| 5 | fjzse | 减征税额 | numeric | 23 | 10 | √ | 0 | 减征税额 |
| 6 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 7 | famount | 销售收入 | numeric | 23 | 10 | √ | 0 | 销售收入 |
| 8 | ftaxmethod | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式,枚举: 1 :一般计税 2 :简易计税 |
| 9 | fjzjt | 即征即退业务 | varchar | 50 |  | √ | ' ' | 即征即退业务,枚举: 0 :否 1 :是 |
| 10 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 11 | fybtse | 应补退税额 | numeric | 23 | 10 | √ | 0 | 应补退税额 |
| 12 | ftype | 类别 | varchar | 50 |  | √ | ' ' | 类别,枚举: 1 :一般货物及劳务 2 :应税服务 |
| 13 | fsuborgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 15 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 16 | fdktaxamount | 进项实际抵扣税额 | numeric | 23 | 10 | √ | 0 | 进项实际抵扣税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_ybhz_zlb_sehfjt |  | forgid,fstartdate,fenddate |
| 2 | pk_tcvat_ybhz_zlb_sehfjt |  | fid |
