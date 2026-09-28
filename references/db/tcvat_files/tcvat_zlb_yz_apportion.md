# 汇总预征二级机构税额分摊表单据-tcvat_zlb_yz_apportion

## 汇总预征二级机构税额分摊表单据-主表 t_tcvat_zlb_yz_apportion

- **表名称：** 汇总预征二级机构税额分摊表单据-主表
- **表名：** t_tcvat_zlb_yz_apportion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnormaltaxsale | 一般计税销售额 | numeric | 23 | 10 | √ | 0 | 一般计税销售额 |
| 3 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 4 | fsimpletaxamount | 简易计税税额 | numeric | 23 | 10 | √ | 0 | 简易计税税额 |
| 5 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: |
| 8 | fnormaltaxamount | 一般计税分配税额 | numeric | 23 | 10 | √ | 0 | 一般计税分配税额 |
| 9 | fsuborg | 汇总方案组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | ftotaltaxamount | 合计税额 | numeric | 23 | 10 | √ | 0 | 合计税额 |
| 11 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 4 :4级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_zlb_yz_apportion |  | fid |
| 2 | idx_t_tcvat_zlb_yz_apportion1 |  | forgid,fstartdate,fenddate |
