# 二级机构税额分摊（一般货物和应税服务）-tcvat_zlb_yz_ejjgseft

## 二级机构税额分摊（一般货物和应税服务）-主表 t_tcvat_zlb_yz_ejjgseft

- **表名称：** 二级机构税额分摊（一般货物和应税服务）-主表
- **表名：** t_tcvat_zlb_yz_ejjgseft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主数据id | int8 | 64 |  | √ | 0 | 主数据id |
| 2 | fparentid | 上级组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fysfwjzjtfpse | 应税服务即征即退-分配税额 | numeric | 23 | 10 | √ | 0 | 应税服务即征即退-分配税额 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fysfwfpse | 应税服务-分配税额 | numeric | 23 | 10 | √ | 0 | 应税服务-分配税额 |
| 6 | fysfwjzjtxssr | 应税服务即征即退-销售收入 | numeric | 23 | 10 | √ | 0 | 应税服务即征即退-销售收入 |
| 7 | ffpse | 一般货物及劳务-分配税额 | numeric | 23 | 10 | √ | 0 | 一般货物及劳务-分配税额 |
| 8 | fjzjtxssr | 一般货物及劳务即征即退-销售收入 | numeric | 23 | 10 | √ | 0 | 一般货物及劳务即征即退-销售收入 |
| 9 | fysfwfpbl | 应税服务-分配比例 | numeric | 23 | 10 | √ | 0 | 应税服务-分配比例 |
| 10 | fjzjtfpse | 一般货物及劳务即征即退-分配税额 | numeric | 23 | 10 | √ | 0 | 一般货物及劳务即征即退-分配税额 |
| 11 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 12 | fxssr | 一般货物及劳务-销售收入 | numeric | 23 | 10 | √ | 0 | 一般货物及劳务-销售收入 |
| 13 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 14 | ffpbl | 一般货物及劳务-分配比例 | numeric | 23 | 10 | √ | 0 | 一般货物及劳务-分配比例 |
| 15 | fjzjtfpbl | 一般货物及劳务即征即退-分配比例 | numeric | 23 | 10 | √ | 0 | 一般货物及劳务即征即退-分配比例 |
| 16 | fysfwxssr | 应税服务-销售收入 | numeric | 23 | 10 | √ | 0 | 应税服务-销售收入 |
| 17 | fysfwjzjtfpbl | 应税服务即征即退-分配比例 | numeric | 23 | 10 | √ | 0 | 应税服务即征即退-分配比例 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fsuborg | 汇总方案组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_zlb_yz_ejjgseft |  | forgid,fstartdate,fenddate |
| 2 | idx_t_tcvat_zlb_yz_ejjgseft_id |  | fid |
| 3 | pk_tcvat_zlb_yz_ejjgseft |  | fentryid |
