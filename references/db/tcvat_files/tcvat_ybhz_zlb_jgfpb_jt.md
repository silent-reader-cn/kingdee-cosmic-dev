# 一般汇总总览表机构分配表_计提-tcvat_ybhz_zlb_jgfpb_jt

## 一般汇总总览表机构分配表_计提-主表 t_tcvat_ybhz_zlb_jgfpb_jt

- **表名称：** 一般汇总总览表机构分配表_计提-主表
- **表名：** t_tcvat_ybhz_zlb_jgfpb_jt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fysfwjzjtfpse | 应税服务即征即退分配税额 | numeric | 23 | 10 | √ | 0 | 应税服务即征即退分配税额 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fysfwfpse | 应税服务分配税额 | numeric | 23 | 10 | √ | 0 | 应税服务分配税额 |
| 5 | fsuborgname | 组织名称 | varchar | 500 |  | √ | ' ' | 组织名称 |
| 6 | fysfwjzjtxssr | 应税服务即征即退销售收入 | numeric | 23 | 10 | √ | 0 | 应税服务即征即退销售收入 |
| 7 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 8 | fdeclaration | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :独立 2 :汇总 3 :被汇总 |
| 9 | ffpse | 一般货物及劳务分配税额 | numeric | 23 | 10 | √ | 0 | 一般货物及劳务分配税额 |
| 10 | fjzjtxssr | 一般货物及劳务即征即退销售收入 | numeric | 23 | 10 | √ | 0 | 一般货物及劳务即征即退销售收入 |
| 11 | fysfwfpbl | 应税服务分配比例 | numeric | 23 | 10 |  | null | 应税服务分配比例 |
| 12 | fjzjtfpse | 一般货物及劳务即征即退分配税额 | numeric | 23 | 10 | √ | 0 | 一般货物及劳务即征即退分配税额 |
| 13 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 14 | fxssr | 一般货物及劳务销售收入 | numeric | 23 | 10 | √ | 0 | 一般货物及劳务销售收入 |
| 15 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 16 | fsuborgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | ffpbl | 一般货物及劳务分配比例 | numeric | 23 | 10 |  | null | 一般货物及劳务分配比例 |
| 18 | fjzjtfpbl | 一般货物及劳务即征即退分配比例 | numeric | 23 | 10 |  | null | 一般货物及劳务即征即退分配比例 |
| 19 | fysfwxssr | 应税服务销售收入 | numeric | 23 | 10 | √ | 0 | 应税服务销售收入 |
| 20 | fpbsehj | 分配税额合计 | numeric | 23 | 10 | √ | 0 | 分配税额合计 |
| 21 | fysfwjzjtfpbl | 应税服务即征即退分配比例 | numeric | 23 | 10 |  | null | 应税服务即征即退分配比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_ybhz_zlb_jgfpbjt |  | forgid,fstartdate,fenddate |
| 2 | pk_tcvat_ybhz_zlb_jgfpbjt |  | fid |
