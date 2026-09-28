# 日志注册-bos_ctlog_register

## 日志注册-主表 t_ctlog_register

- **表名称：** 日志注册-主表
- **表名：** t_ctlog_register

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 日志名称 | varchar | 255 |  | √ | ' ' | 日志名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fenablemservice | 微服务取数 | bpchar | 1 |  | √ | '0' | 微服务取数 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | frouteapp | 微服务路由应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 7 | fisvkey | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fenable | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fplugin | 取数插件 | varchar | 2000 |  | √ | ' ' | 取数插件 |
| 14 | fnumber | 日志编码 | varchar | 50 |  | √ | ' ' | 日志编码 |
| 15 | flogform | 日志详情表单 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctlog_register_number |  | fnumber |
| 2 | pk_ctlog_register |  | fid |

---

## 日志状态单据体-子表 t_ctlog_register_status

- **表名称：** 日志状态单据体-子表
- **表名：** t_ctlog_register_status

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstatuslevel | 状态等级 | bpchar | 1 |  | √ | '0' | 状态等级,枚举: 1 :绿色执行成功 2 :红色执行失败 0 :橙色警告未执行 3 :蓝色进行中 |
| 3 | fstatusdesc | 状态描述 | varchar | 255 |  | √ | ' ' | 状态描述 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fstatusvalue | 状态值 | varchar | 50 |  | √ | ' ' | 状态值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ctlog_register_status |  | fentryid |

---

## 日志注册-多语言表 t_ctlog_register_l

- **表名称：** 日志注册-多语言表
- **表名：** t_ctlog_register_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 日志名称 | varchar | 255 |  | √ | ' ' | 日志名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ctlog_register_l |  | fpkid |

---

## 日志状态单据体-多语言表 t_ctlog_register_status_l

- **表名称：** 日志状态单据体-多语言表
- **表名：** t_ctlog_register_status_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fstatusdesc | 状态描述 | varchar | 255 |  | √ | ' ' | 状态描述 |
| 2 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ctlog_register_status_l |  | fpkid |
