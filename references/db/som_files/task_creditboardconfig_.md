# 信用看板单据映射配置-task_creditboardconfig_

## 信用看板单据映射配置-多语言表 t_tk_creditboardconfig_l

- **表名称：** 信用看板单据映射配置-多语言表
- **表名：** t_tk_creditboardconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_creboacon_l_flocaleid |  | fid,flocaleid |
| 2 | pk_t_tk_creditboardconfig_l |  | fpkid |

---

## 信用看板单据映射配置-主表 t_tk_creditboardconfig

- **表名称：** 信用看板单据映射配置-主表
- **表名：** t_tk_creditboardconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | ffieldname | 业务类型取值字段 | varchar | 50 |  | √ | ' ' | 业务类型取值字段 |
| 7 | fdescription | fdescription | varchar | 255 |  |  | null |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fctrlstrategy | fctrlstrategy | varchar | 10 |  | √ | ' ' |  |
| 10 | ffieldnumber | 业务类型取值字段标识 | varchar | 50 |  | √ | ' ' | 业务类型取值字段标识 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | ffieldentitynumber | 业务类型取值字段实体标识 | varchar | 50 |  | √ | ' ' | 业务类型取值字段实体标识 |
| 16 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |
| 17 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_creditboardconfig |  | fid |
| 2 | idx_ssc_creboacon_fcreorgid |  | fcreateorgid |
