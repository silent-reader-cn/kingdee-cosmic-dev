# 项目日志单据字段登记-mpm_billfieldregistlog

## 删除记录单据体-子表 t_mpm_delfieldentry

- **表名称：** 删除记录单据体-子表
- **表名：** t_mpm_delfieldentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelyonvalue | 依赖字段值 | varchar | 512 |  | √ | ' ' | 依赖字段值 |
| 3 | frelyonfield | 依赖字段 | varchar | 255 |  | √ | ' ' | 依赖字段 |
| 4 | fvaluefield | 取值字段 | varchar | 255 |  | √ | ' ' | 取值字段 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_delfieldentry |  | fentryid |
| 2 | idx_mpm_delfieldentry_fk |  | fid |

---

## 项目日志单据字段登记-主表 t_mpm_fieldregistlog

- **表名称：** 项目日志单据字段登记-主表
- **表名：** t_mpm_fieldregistlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | frelationfield | 关联记录字段 | varchar | 255 |  | √ | ' ' | 关联记录字段 |
| 6 | fconditionjson | 记录条件(json) | varchar | 2000 |  | √ | ' ' | 记录条件(json) |
| 7 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | flogobjectid | 对应的日志对象 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fbizobjectid | 变更的业务对象 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fshownamesign | 显示名称字段标识 | varchar | 255 |  | √ | '' | 显示名称字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_fieldregistlog_fn |  | fnumber |
| 2 | pk_mpm_fieldregistlog |  | fid |

---

## 字段登记-子表 t_mpm_logfieldentry

- **表名称：** 字段登记-子表
- **表名：** t_mpm_logfieldentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fregentrysign | 分录标识 | varchar | 512 |  | √ | ' ' | 分录标识 |
| 3 | fgroupby | 分类 | varchar | 3 |  | √ | ' ' | 分类,枚举: A :项目基本信息 B :项目团队 C :任务基本信息 D :任务依赖关系 E :交付物料 F :交付文档 G :项目变更 |
| 4 | fisrecordlog | 记录日志 | bpchar | 1 |  | √ | '0' | 记录日志 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ffieldsign | 字段 | varchar | 512 |  | √ | ' ' | 字段 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_logfieldentry |  | fentryid |
| 2 | idx_mpm_logfieldentry |  | fid |

---

## 关联的日志对象-多选基础资料表 t_mpm_rellogobject

- **表名称：** 关联的日志对象-多选基础资料表
- **表名：** t_mpm_rellogobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_rellogobject |  | fpkid |
| 2 | idx_mpm_rellogobject_fi |  | fid |

---

## 项目日志单据字段登记-多语言表 t_mpm_fieldregistlog_l

- **表名称：** 项目日志单据字段登记-多语言表
- **表名：** t_mpm_fieldregistlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_fieldregistlog_l_fl |  | fid,flocaleid |
| 2 | pk_mpm_fieldregistlog_l |  | fpkid |
