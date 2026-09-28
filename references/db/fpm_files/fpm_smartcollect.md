# 业务数据采集方案-fpm_smartcollect

## 字段映射单据体-子表 t_fpm_fieldmapping

- **表名称：** 字段映射单据体-子表
- **表名：** t_fpm_fieldmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgetvaluedesc | 取值表达式 | varchar | 1024 |  | √ | ' ' | 取值表达式 |
| 3 | fgetvaluesave | 取值表达式（存储） | varchar | 1024 |  | √ | ' ' | 取值表达式（存储） |
| 4 | fsourcefieldsave_tag | 来源单字段 | varchar | 255 |  | √ | ' ' | 来源单字段,枚举: |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftargetfielddesc | 目标字段 | varchar | 255 |  | √ | ' ' | 目标字段 |
| 7 | fvaltype | 取值类型 | varchar | 50 |  | √ | ' ' | 取值类型,枚举: SOURCE_FIELD :源单字段 CALC_FORMULA :计算公式 CONSTANT :常量 |
| 8 | fgetvaluesave_tag | 取值表达式（存储）_详情 | text | 0 |  |  | null | 取值表达式（存储）_详情 |
| 9 | fmustinput | 是否必录 | bpchar | 1 |  | √ | '1' | 是否必录 |
| 10 | fsync | 开启源单字段值变化监听 | bpchar | 1 |  | √ | '0' | 开启源单字段值变化监听 |
| 11 | fisintercept | 取值超长是否截取 | bpchar | 1 |  | √ | '0' | 取值超长是否截取 |
| 12 | fsourcefielddesc | fsourcefielddesc | varchar | 255 |  | √ | ' ' |  |
| 13 | fjudgeunique | 数据判断规则唯一值 | bpchar | 1 |  | √ | '1' | 数据判断规则唯一值 |
| 14 | ftargetfieldprop | 目标字段标识 | varchar | 255 |  | √ | ' ' | 目标字段标识 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fsyncprop | 监听的源单字段 | varchar | 2000 |  | √ | ' ' | 监听的源单字段,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_fieldmapping |  | fid |
| 2 | pk_t_fpm_fieldmapping |  | fentryid |

---

## 适用组织单据体-子表 t_fpm_applyorg

- **表名称：** 适用组织单据体-子表
- **表名：** t_fpm_applyorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | forg | 业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_applyorg |  | fentryid |
| 2 | inx_fpm_applyorg |  | fid |

---

## 数据自动更新方案配置-子表 t_fpm_smartcollectop

- **表名称：** 数据自动更新方案配置-子表
- **表名：** t_fpm_smartcollectop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsyncimm | 开启实时更新 | bpchar | 1 |  | √ | '0' | 开启实时更新 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fstrategy | 目标单处理策略 | varchar | 60 |  | √ | ' ' | 目标单处理策略,枚举: update :更新目标单 discard :废弃目标单 |
| 5 | fsyncoperatename | 源单监听操作 | varchar | 2000 |  | √ | ' ' | 源单监听操作 |
| 6 | fsyncoperatekey | 源单监听操作标识 | varchar | 2000 |  | √ | ' ' | 源单监听操作标识 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_smartcollectop_fid |  | fid |
| 2 | pk_t_fpm_smartcollectop |  | fentryid |

---

## 业务数据采集方案-多语言表 t_fpm_smartcollect_l

- **表名称：** 业务数据采集方案-多语言表
- **表名：** t_fpm_smartcollect_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 3 | fname | 模板名称 | varchar | 255 |  | √ | ' ' | 模板名称 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_smartcollect_l |  | fpkid |
| 2 | idx_dpm_smartcollect_l |  | fid |

---

## 业务数据采集方案-主表 t_fpm_smartcollect

- **表名称：** 业务数据采集方案-主表
- **表名：** t_fpm_smartcollect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 模板名称 | varchar | 100 |  | √ | ' ' | 模板名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | flinkentity | 取数关联实体 | varchar | 100 |  | √ | ' ' | 取数关联实体,枚举: |
| 7 | fsourcebill | 来源业务单据 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fapplycondition | 适用条件 | varchar | 1024 |  | √ | ' ' | 适用条件 |
| 10 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsaveapplycondition | 适用条件（存储） | varchar | 1024 |  | √ | ' ' | 适用条件（存储） |
| 14 | fsaveapplycondition_tag | 适用条件（存储）_详情 | text | 0 |  |  | null | 适用条件（存储）_详情 |
| 15 | fpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 16 | ftargetbill | 目标单据 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 模板编码 | varchar | 50 |  | √ | ' ' | 模板编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_smartcollect |  | fid |
| 2 | idx_fpm_smartcollect |  | fnumber |
