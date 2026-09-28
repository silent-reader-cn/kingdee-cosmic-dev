# 状态规则-mpdm_staterule

## 单据体-更新方式-子表 t_mpdm_staterulemm

- **表名称：** 单据体-更新方式-子表
- **表名：** t_mpdm_staterulemm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fleftbracket |  | varchar | 5 |  | √ | ' ' | ,枚举: ( :( (( :(( ((( :((( |
| 3 | fconditionalfilterdesc | 条件过滤 | varchar | 2000 |  | √ | ' ' | 条件过滤 |
| 4 | frightbracket |  | varchar | 5 |  | √ | ' ' | ,枚举: ) :) )) :)) ))) :))) |
| 5 | fmmbill | 实体 | varchar | 255 |  | √ | 0 | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fcalculationformula_tag | 计算公式(jjson)_详情 | text | 0 |  |  | ' ' | 计算公式(jjson)_详情 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | flogic | 逻辑 | varchar | 5 |  | √ | ' ' | 逻辑,枚举: and :并且 or :或者 |
| 9 | fcalculationformuladesc | 计算公式 | varchar | 2000 |  | √ | ' ' | 计算公式 |
| 10 | fcalculationformula | 计算公式(jjson) | varchar | 2000 |  | √ | ' ' | 计算公式(jjson) |
| 11 | finspectionscope | 检查范围 | varchar | 5 |  | √ | ' ' | 检查范围,枚举: 1 :全部 2 :等于 |
| 12 | fmatchattribute | 匹配属性 | varchar | 50 |  | √ | ' ' | 匹配属性 |
| 13 | fconditionalfilter_tag | 条件过滤(json)_详情 | text | 0 |  |  | ' ' | 条件过滤(json)_详情 |
| 14 | fconditionalfilter | 条件过滤(json) | varchar | 2000 |  | √ | ' ' | 条件过滤(json) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_statmm_fid |  | fid |
| 2 | idx_mpdm_statmm_fseq |  | fseq |
| 3 | pk_mpdm_staterulemm |  | fentryid |

---

## 单据体-业务触发-子表 t_mpdm_staterulebt

- **表名称：** 单据体-业务触发-子表
- **表名：** t_mpdm_staterulebt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbtapp | 应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 3 | fbttriggertype | 触发类型 | varchar | 5 |  | √ | ' ' | 触发类型,枚举: A :微服务 B :业务事件中心 |
| 4 | fbttriggerevent | 触发事件服务 | varchar | 100 |  | √ | ' ' | 触发事件服务 |
| 5 | fbtbill | 实体 | varchar | 255 |  | √ | 0 | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbtmethod | 方法 | varchar | 50 |  | √ | ' ' | 方法 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbtcloud | 云 | varchar | 50 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_statbt_fid |  | fid |
| 2 | pk_mpdm_staterulebt |  | fentryid |
| 3 | idx_mpdm_statbt_fseq |  | fseq |

---

## 单据体-业务控制-子表 t_mpdm_staterulebc

- **表名称：** 单据体-业务控制-子表
- **表名：** t_mpdm_staterulebc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbcconditionalfilter_tag | 条件过滤(json)_详情 | text | 0 |  |  | ' ' | 条件过滤(json)_详情 |
| 3 | fbcoperationobject | 操作对象 | varchar | 50 |  | √ | ' ' | 操作对象 |
| 4 | fbcconditionalfilter | 条件过滤(json) | varchar | 2000 |  | √ | ' ' | 条件过滤(json) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbcbill | 实体 | varchar | 255 |  | √ | 0 | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fbcconditionalfilterdesc | 条件过滤 | varchar | 2000 |  | √ | ' ' | 条件过滤 |
| 8 | fbccontroltype | 控制类型 | varchar | 5 |  | √ | ' ' | 控制类型,枚举: A :功能操作 B :字段修改 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fbcmatchattribute | 匹配属性 | varchar | 50 |  | √ | ' ' | 匹配属性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_staterulebc |  | fentryid |
| 2 | idx_mpdm_statbc_fid |  | fid |
| 3 | idx_mpdm_statbc_fseq |  | fseq |

---

## 状态规则-主表 t_mpdm_staterule

- **表名称：** 状态规则-主表
- **表名：** t_mpdm_staterule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbillstate | 目标状态 | int8 | 64 |  | √ | 0 | [项目状态 bd_projectstatus](../basedata_files/bd_projectstatus.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 10 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 11 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fname | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fbill | 目标实体 | varchar | 255 |  | √ | 0 | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fbillfield | 目标字段(json) | varchar | 50 |  | √ | ' ' | 目标字段(json) |
| 17 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 18 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 19 | fbillfielddesc | 目标字段 | varchar | 50 |  | √ | ' ' | 目标字段 |
| 20 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 规则编码 | varchar | 30 |  | √ | ' ' | 规则编码 |
| 22 | fdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fcombofield | 更新方式 | varchar | 5 |  | √ | ' ' | 更新方式,枚举: A :人工 B :自动 C :人工+自动 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_staterule_createorg |  | fcreateorgid |
| 2 | pk_mpdm_staterule |  | fid |
| 3 | idx_mpdm_statle_fcreatetime |  | fcreatetime |
| 4 | idx_mpdm_statle_fnumber |  | fnumber |
| 5 | idx_t_mpdm_staterule_master |  | fmasterid |

---

## 状态规则-使用范围位图表 t_mpdm_staterule_m

- **表名称：** 状态规则-使用范围位图表
- **表名：** t_mpdm_staterule_m

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
| 1 | pk_t_mpdm_staterule_m |  | forgid |

---

## 状态规则-多语言表 t_mpdm_staterule_l

- **表名称：** 状态规则-多语言表
- **表名：** t_mpdm_staterule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_statlel_fid |  | fid,flocaleid |
| 2 | pk_mpdm_staterule_l |  | fpkid |
| 3 | idx_mpdm_statlel_fname |  | fname |

---

## 状态规则-使用范围表 t_mpdm_staterule_u

- **表名称：** 状态规则-使用范围表
- **表名：** t_mpdm_staterule_u

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
| 1 | idx_t_mpdm_staterule_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_staterule_u |  | fdataid,fuseorgid |
