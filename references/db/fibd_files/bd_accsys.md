# 核算体系实体-bd_accsys

## 委托组织分录关系-子表 t_bd_orgrelationship

- **表名称：** 委托组织分录关系-子表
- **表名：** t_bd_orgrelationship

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgentryid | 委托组织的id | int8 | 64 |  | √ | 0 | 委托组织的id |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_orgrelationship |  | fentryid |
| 2 | idx_bd_orgrelationship |  | fid |

---

## 核算体系实体-主表 t_bd_accountsys

- **表名称：** 核算体系实体-主表
- **表名：** t_bd_accountsys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmainviewid | 主视图视图id | int8 | 64 |  | √ | 0 | 主视图视图id |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 5 | fdesc | 描述 | varchar | 50 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_accountsys |  | fid |
| 2 | idx_bd_accountsys |  | fmainviewid |

---

## 账簿关系-子表 t_bd_bookrelationship

- **表名称：** 账簿关系-子表
- **表名：** t_bd_bookrelationship

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fbookid | 账簿id | int8 | 64 |  | √ | 0 | 账簿id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_bookrelationship |  | fentryid |
| 2 | idx_bd_bookrelationship |  | fid |

---

## 单据体-多语言表 t_bd_orgviewrelationship_l

- **表名称：** 单据体-多语言表
- **表名：** t_bd_orgviewrelationship_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fstatname | 统计视图名称 | varchar | 50 |  | √ | ' ' | 统计视图名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_orgviewrelation_locale |  | fentryid,flocaleid |
| 2 | pk_t_bd_orgviewrelationship_l |  | fpkid |

---

## 单据体-子表 t_bd_orgviewrelationship

- **表名称：** 单据体-子表
- **表名：** t_bd_orgviewrelationship

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fstatviewid | 统计视图视图id | int8 | 64 |  | √ | 0 | 统计视图视图id |
| 5 | fstatname | 统计视图名称 | varchar | 50 |  | √ | ' ' | 统计视图名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_orgviewrelationship |  | fid |
| 2 | pk_t_bd_orgviewrelationship |  | fentryid |

---

## 核算体系实体-多语言表 t_bd_accountsys_l

- **表名称：** 核算体系实体-多语言表
- **表名：** t_bd_accountsys_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_accountsys_locale |  | fid,flocaleid |
| 2 | pk_t_bd_accountsys_l |  | fpkid |
