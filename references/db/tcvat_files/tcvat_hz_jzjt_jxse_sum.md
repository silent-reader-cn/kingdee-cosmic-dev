# 总机构即征即退进项税额底稿-tcvat_hz_jzjt_jxse_sum

## 总机构即征即退进项税额底稿-主表 t_tcvat_hz_jzjt_jxse_sum

- **表名称：** 总机构即征即退进项税额底稿-主表
- **表名：** t_tcvat_hz_jzjt_jxse_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjzjtjxtax | 即征即退进项税额 | numeric | 23 | 10 | √ | 0 | 即征即退进项税额 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fsuborgname | fsuborgname | varchar | 50 |  | √ | ' ' |  |
| 8 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: |
| 9 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 10 | fjzjtlx | 即征即退类型 | varchar | 50 |  | √ | ' ' | 即征即退类型,枚举: jzjt :即征即退 wfhf :无法划分 |
| 11 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 12 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 13 | finputtax | 进项税额 | numeric | 23 | 10 | √ | 0 | 进项税额 |
| 14 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 15 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 16 | fsuborgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fjzjtamount | 即征即退销售额 | numeric | 23 | 10 | √ | 0 | 即征即退销售额 |
| 18 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 19 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 20 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 21 | famountsum | 销售额合计 | numeric | 23 | 10 | √ | 0 | 销售额合计 |
| 22 | fsplitrate | 划分比例 | numeric | 23 | 10 | √ | 0 | 划分比例 |
| 23 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 4 :4级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_hz_jzjt_jxse_sum |  | fid |
| 2 | idx_tcvat_hz_jzjt_jxse_sum_1 |  | forgid,fstartdate,fenddate |
