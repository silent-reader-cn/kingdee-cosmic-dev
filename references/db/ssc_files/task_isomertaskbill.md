# 通用审核单-task_isomertaskbill

## 通用审核单-主表 t_tk_isomertaskbill

- **表名称：** 通用审核单-主表
- **表名：** t_tk_isomertaskbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foriginalbillno | 原单单据编号 | varchar | 50 |  | √ | ' ' | 原单单据编号 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fimagestatus | 影像状态 | varchar | 4 |  | √ | ' ' | 影像状态 |
| 5 | fbillstatus | 单据状态 | varchar | 4 |  | √ | ' ' | 单据状态,枚举: B :已提交 C :审核中 D :审核通过 E :审核不通过 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fisomertasktypeid | 通用审核单类型 | int8 | 64 |  | √ | 0 | [通用审核单类型 task_isomertasktype](../ssc_files/task_isomertasktype.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fapplicant | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | foriginalsystemid | 来源系统 | int8 | 64 |  | √ | 0 | [业务系统 bas_extenderp](../sys_files/bas_extenderp.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | foriginalstatus | 原单据状态 | varchar | 4 |  | √ | ' ' | 原单据状态 |
| 14 | foriginalink | foriginalink | varchar | 1024 |  | √ | ' ' |  |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fimagelink | 影像链接 | varchar | 1024 |  | √ | ' ' | 影像链接 |
| 17 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_isomertaskbill |  | fid |
| 2 | idx_ssc_isotaskbill_createtime |  | fcreatetime |
| 3 | idx_ssc_isotaskbill_num |  | fbillno |
