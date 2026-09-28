# 内容包安装申请记录-iprm_resourceinstalllist

## 内容包安装申请记录-主表 t_iprm_resourceinstall

- **表名称：** 内容包安装申请记录-主表
- **表名：** t_iprm_resourceinstall

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 0 :已提交 1 :等待安装 2 :安装成功 3 :安装失败 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fexceptioninfo | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fapplytime | 申请日期 | varchar | 30 |  | √ | ' ' | 申请日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | finstalltime | 安装日期 | varchar | 30 |  | √ | ' ' | 安装日期 |
| 12 | fsecuritycode | 关联安全码 | varchar | 30 |  | √ | ' ' | 关联安全码 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iprm_res_billno |  | fbillno |
| 2 | pk_t_iprm_resourceinstall |  | fid |
