# 申报项目信息-rdem_sbxmxx

## 申报项目信息-主表 t_rdem_sbxmxx

- **表名称：** 申报项目信息-主表
- **表名：** t_rdem_sbxmxx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 申报项目名称 | varchar | 200 |  | √ | ' ' | 申报项目名称 |
| 4 | fstart | 项目起始时间 | timestamp | 0 |  |  | null | 项目起始时间 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fpurpose | 项目用途 | varchar | 50 |  | √ | ' ' | 项目用途,枚举: jjkc :加计扣除 gqrd :高新认定 |
| 8 | feprojectstatus | 项目状态 | varchar | 50 |  | √ | ' ' | 项目状态,枚举: 0 :未完成 1 :已完成 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :模板导入 2 :手工新增 3 :系统同步 4 :系统生成 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fend | 项目结束时间 | timestamp | 0 |  |  | null | 项目结束时间 |
| 16 | fnumber | 申报项目编号 | varchar | 200 |  | √ | ' ' | 申报项目编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_sbxmxx_m0 |  | fmasterid |
| 2 | pk_rdem_sbxmxx |  | fid |

---

## 关联研发项目-子表 t_rdem_sbxmxx_entry

- **表名称：** 关联研发项目-子表
- **表名：** t_rdem_sbxmxx_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedatapropfield61 | fbasedatapropfield61 | varchar | 50 |  | √ | ' ' |  |
| 3 | fbasedatapropfield51 | fbasedatapropfield51 | varchar | 50 |  | √ | ' ' |  |
| 4 | fyfxmxxid | 研发项目编码 | int8 | 64 |  | √ | 0 | [研发项目信息 rdem_yfxmxx](../rdem_files/rdem_yfxmxx.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbaseproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_sbxmxx_entry |  | fentryid |
| 2 | idx_rdem_sbxmxx_entry_fk |  | fid |

---

## 申报项目信息-多语言表 t_rdem_sbxmxx_l

- **表名称：** 申报项目信息-多语言表
- **表名：** t_rdem_sbxmxx_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 申报项目名称 | varchar | 300 |  | √ | ' ' | 申报项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_sbxmxx_l_0 |  | fid,flocaleid |
| 2 | pk_rdem_sbxmxx_l |  | fpkid |
