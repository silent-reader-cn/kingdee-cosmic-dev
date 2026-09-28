# 汇总预征二级机构分配比例单据-tcvat_zlb_yz_share_ratio

## 汇总预征二级机构分配比例单据-主表 t_tcvat_zlb_yz_share_rati

- **表名称：** 汇总预征二级机构分配比例单据-主表
- **表名：** t_tcvat_zlb_yz_share_rati

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 3 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fysxse | 一般计税方法应税销售额 | numeric | 23 | 10 | √ | 0 | 一般计税方法应税销售额 |
| 6 | ffpbl | 二级机构分配比例 | numeric | 23 | 10 | √ | 0 | 二级机构分配比例 |
| 7 | fynse | 一般计税方法应纳税额 | numeric | 23 | 10 | √ | 0 | 一般计税方法应纳税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_zlb_yz_share_rati |  | fid |
| 2 | idx_t_tcvat_zlb_yz_share_ra1 |  | forgid,fstartdate,fenddate |
