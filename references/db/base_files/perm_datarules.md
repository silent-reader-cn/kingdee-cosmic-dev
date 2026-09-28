# 数据规则方案集合-perm_datarules

## 数据规则方案集合-主表 t_perm_datarules

- **表名称：** 数据规则方案集合-主表
- **表名：** t_perm_datarules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fdataruleid | 全局数据规则 | int8 | 64 |  | √ | 0 | 数据规则方案 perm_datarule |
| 10 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_datarules_pkey |  | fid |
| 2 | idx_perm_datarules |  | fnumber |

---

## 单据体-子表 t_perm_datarules_entry

- **表名称：** 单据体-子表
- **表名：** t_perm_datarules_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentitynum | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdataruleid | 数据规则 | int8 | 64 |  | √ | 0 | 数据规则方案 perm_datarule |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_datarules_entry |  | fid,fbizappid,fentitynum |
| 2 | t_perm_datarules_entry_pkey |  | fentryid |

---

## 数据规则方案集合-多语言表 t_perm_datarules_l

- **表名称：** 数据规则方案集合-多语言表
- **表名：** t_perm_datarules_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_datarules_l_pkey |  | fpkid |
| 2 | idx_perm_datarules_l |  | fid,flocaleid |
