# 制造策略维度配置-bd_manustrconfig

## 追溯范围-子表 t_bd_manustrconfigentry

- **表名称：** 追溯范围-子表
- **表名：** t_bd_manustrconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdomainid | 领域 | int8 | 64 |  | √ | 0 | 制造策略领域(供应链) bd_manustrategydomain |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fbillentityid | 单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fisupdateinv | 更新库存 | bpchar | 1 |  | √ | '0' | 更新库存 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_manustrconfigentry |  | fid,fseq |
| 2 | pk_t_bd_manustrconfigentry |  | fentryid |

---

## 制造策略维度配置-主表 t_bd_manustrconfig

- **表名称：** 制造策略维度配置-主表
- **表名：** t_bd_manustrconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 10 | fispreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_manustrconfig |  | fid |
| 2 | idx_bd_manustrconfig |  | fnumber |

---

## 追溯维度-子表 t_bd_manustrconfigentrye

- **表名称：** 追溯维度-子表
- **表名：** t_bd_manustrconfigentrye

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdimensionid | 维度编码 | int8 | 64 |  | √ | 0 | 制造策略维度 bd_manustrategydim |
| 2 | ffield | 映射字段 | varchar | 100 |  | √ | ' ' | 映射字段 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_manustrconfigentrye |  | fentryid,fseq |
| 2 | pk_t_bd_manustrconfigentrye |  | fdetailid |

---

## 制造策略维度配置-多语言表 t_bd_manustrconfig_l

- **表名称：** 制造策略维度配置-多语言表
- **表名：** t_bd_manustrconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_manustrconfig_l |  | fid,flocaleid |
| 2 | pk_t_bd_manustrconfig_l |  | fpkid |
