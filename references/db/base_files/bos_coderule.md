# 编码规则-bos_coderule

## 编码组织-子表 t_cr_apporg

- **表名称：** 编码组织-子表
- **表名：** t_cr_apporg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fisincludesuborg | 包含下级 | bpchar | 1 |  | √ | ' ' | 包含下级 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cr_apporg_pkey |  | fentryid |
| 2 | idx_t_cr_apporg_fid |  | fid,forgid |

---

## 编码规则-多语言表 t_cr_coderule_l

- **表名称：** 编码规则-多语言表
- **表名：** t_cr_coderule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 规则名称 | varchar | 255 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cr_coderule_l_pkey |  | fpkid |
| 2 | idx_t_cr_coderule_l_fname |  | fname |
| 3 | idx_t_cr_coderule_l_fid |  | fid,flocaleid |

---

## 单据体-子表 t_cr_appcondition

- **表名称：** 单据体-子表
- **表名：** t_cr_appcondition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fpropertyvalue | 属性值 | varchar | 100 |  | √ | ' ' | [适用条件属性值 bos_crappcondprovalue](../base_files/bos_crappcondprovalue.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fproperty | 属性 | varchar | 100 |  | √ | ' ' | [适用条件属性 bos_coderuleappcondpro](../base_files/bos_coderuleappcondpro.md) |
| 5 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cr_appcondition_fcrid |  | fid |
| 2 | t_cr_appcondition_pkey |  | fentryid |

---

## 编码规则-主表 t_cr_coderule

- **表名称：** 编码规则-主表
- **表名：** t_cr_coderule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fisfast | 高性能 | bpchar | 1 |  | √ | '0' | 高性能 |
| 3 | fisnonbreak | 断号补偿 | bpchar | 1 |  | √ | '0' | 断号补偿 |
| 4 | fisappcondition | 适用条件 | bpchar | 1 |  | √ | '0' | 适用条件 |
| 5 | fisapporg | 受控组织 | bpchar | 1 |  | √ | '0' | 受控组织 |
| 6 | fruletype | fruletype | varchar | 10 |  |  | null |  |
| 7 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 8 | fisupdaterecover | 修改时重新编码 | bpchar | 1 |  | √ | '0' | 修改时重新编码 |
| 9 | fispreset | 预置规则 | bpchar | 1 |  | √ | '0' | 预置规则 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | varchar | 36 |  | √ | ' ' | 主数据内码 |
| 14 | fisunique | 编码唯一性 | bpchar | 1 |  | √ | '0' | 编码唯一性 |
| 15 | fuseinterruption | 消耗断号 | varchar | 10 |  | √ | ' ' | 消耗断号,枚举: 0 :修改编码 1 :导入单据 2 :下推单据 |
| 16 | fisserialnumber | 流水号 | bpchar | 1 |  | √ | '0' | 流水号 |
| 17 | fexample | 编码示例 | varchar | 255 |  | √ | ' ' | 编码示例 |
| 18 | fischecknumber | 校验修改编码的格式 | bpchar | 1 |  | √ | '0' | 校验修改编码的格式 |
| 19 | fsplitsign | 默认段间分隔符 | bpchar | 1 |  | √ | ' ' | 默认段间分隔符,枚举: - :- @ :@ # :# $ :$ % :% ^ :^ & :& * :* _ :_ . :. |
| 20 | ffiltercondition | 启动条件 | text | 0 |  |  | null | 启动条件 |
| 21 | fupdatemaxnumber | 更新最大号 | varchar | 10 |  | √ | ' ' | 更新最大号,枚举: 0 :修改编码 1 :导入单据 2 :下推单据 |
| 22 | fismatchcoderule | 修改的编码消耗断号 | bpchar | 1 |  | √ | '0' | 修改的编码消耗断号 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fisaddview | 新增显示 | bpchar | 1 |  | √ | '0' | 新增显示 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 27 | fctrlmode | 控制方式 | varchar | 10 |  | √ | ' ' | 控制方式,枚举: 1 :组织 2 :控制单元 |
| 28 | fappmode | 应用规则 | varchar | 10 |  | √ | ' ' | 应用规则,枚举: 1 :不允许断号 2 :新增显示 3 :新增显示且允许修改 |
| 29 | fisautoincrlength | 超过设置长度时自动升位 | bpchar | 1 |  | √ | '0' | 超过设置长度时自动升位 |
| 30 | fisfillwithzero | 用0补位 | bpchar | 1 |  | √ | '1' | 用0补位 |
| 31 | fbizobjectid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 32 | fismodifiable | 允许修改 | bpchar | 1 |  | √ | '0' | 允许修改 |
| 33 | fconditiondesc | 启动条件描述 | varchar | 255 |  |  | ' ' | 启动条件描述 |
| 34 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fnumber | 规则编码 | varchar | 80 |  | √ | ' ' | 规则编码 |
| 36 | fischeckcode | 校验码 | bpchar | 1 |  | √ | '0' | 校验码 |
| 37 | fexamplelength | 编码长度 | varchar | 255 |  | √ | ' ' | 编码长度 |
| 38 | fislog | 编码生成日志 | bpchar | 1 |  | √ | '0' | 编码生成日志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cr_coderule_enableobj |  | fbizobjectid,fenable |
| 2 | t_cr_coderule_pkey |  | fid |
| 3 | idx_cr_coderule_num |  | fnumber |

---

## 编码分析-子表 t_cr_coderuleentry

- **表名称：** 编码分析-子表
- **表名：** t_cr_coderuleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fisvisable | 是否显示 | bpchar | 1 |  | √ | ' ' | 是否显示 |
| 3 | fstep | 步长 | int8 | 64 |  | √ | 0 | 步长 |
| 4 | faddstyle | 右侧补位 | bpchar | 1 |  | √ | ' ' | 右侧补位 |
| 5 | flength | 长度 | int8 | 64 |  | √ | 0 | 长度 |
| 6 | fformat | 显示格式 | varchar | 100 |  | √ | ' ' | 显示格式 |
| 7 | finitial | 起始值 | int8 | 64 |  | √ | 0 | 起始值 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fattusingmode | 适用模式 | varchar | 10 |  | √ | ' ' | 适用模式,枚举: 1 :整段编码 2 :分区间段编码 3 :完全取值 4 :属性截断 |
| 10 | fissortitem | 流水号依据 | bpchar | 1 |  | √ | '1' | 流水号依据 |
| 11 | fsettingvalue | 设置值 | varchar | 20 |  | √ | ' ' | 设置值 |
| 12 | faddchar | 补位符 | varchar | 1 |  | √ | ' ' | 补位符 |
| 13 | fvalueatribute | 编码来源 | varchar | 50 |  | √ | ' ' | 编码来源 |
| 14 | fcutstyle | 右侧截取 | bpchar | 1 |  | √ | ' ' | 右侧截取 |
| 15 | fsplitsign | 段间分隔符 | bpchar | 1 |  | √ | '-' | 段间分隔符,枚举: |
| 16 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |
| 17 | fattributetype | 属性类型 | varchar | 10 |  | √ | ' ' | 属性类型,枚举: 1 :常量 2 :创建日期 16 :流水号 4 :文本资料 8 :基础资料 64 :系统资料 |
| 18 | fissplitsign | 段间分隔 | bpchar | 1 |  | √ | '1' | 段间分隔 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cr_coderuleentry_fid |  | fid |
| 2 | t_cr_coderuleentry_pkey |  | fentryid |
