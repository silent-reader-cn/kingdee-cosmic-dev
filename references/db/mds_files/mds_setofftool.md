# 预测冲减运算-mds_setofftool

## 单据体-子表 t_mds_setofftoolentry

- **表名称：** 单据体-子表
- **表名：** t_mds_setofftoolentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifier | fentrymodifier | int8 | 64 |  | √ | 0 |  |
| 3 | fentrycreatedate | fentrycreatedate | timestamp | 0 |  |  | null |  |
| 4 | fsetid | 预测冲减定义编码 | int8 | 64 |  | √ | 0 | 预测冲减定义 mds_setoffsetting |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fisuse | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fentrycreator | fentrycreator | int8 | 64 |  | √ | 0 |  |
| 9 | fentrymodifydate | fentrymodifydate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_setofftoolentry |  | fentryid |
| 2 | idx_mds_setofftoolentry_fid |  | fid |

---

## 预测冲减运算-主表 t_mds_setofftool

- **表名称：** 预测冲减运算-主表
- **表名：** t_mds_setofftool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_setofftool_num |  | fnumber |
| 2 | idx_t_mds_setofftool_createorg |  | fcreateorgid |
| 3 | pk_mds_setofftool |  | fid |
| 4 | idx_t_mds_setofftool_master |  | fmasterid |

---

## 预测冲减运算-多语言表 t_mds_setofftool_l

- **表名称：** 预测冲减运算-多语言表
- **表名：** t_mds_setofftool_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_setofftool_l |  | fpkid |
| 2 | idx_mds_setofftooll_fid |  | fid,flocaleid |

---

## 预测冲减运算-使用范围位图表 t_mds_setofftool_m

- **表名称：** 预测冲减运算-使用范围位图表
- **表名：** t_mds_setofftool_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_setofftool_m |  | forgid |

---

## 预测冲减运算-使用范围表 t_mds_setofftool_u

- **表名称：** 预测冲减运算-使用范围表
- **表名：** t_mds_setofftool_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mds_setofftool_u_uo |  | fuseorgid |
| 2 | pk_t_mds_setofftool_u |  | fdataid,fuseorgid |
