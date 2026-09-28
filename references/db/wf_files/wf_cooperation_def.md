# 工作流协作关系-wf_cooperation_def

## 工作流协作关系-主表 t_wf_cooperationdef

- **表名称：** 工作流协作关系-主表
- **表名：** t_wf_cooperationdef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |
| 4 | fispreinsdata | 是否预置数据 | bpchar | 1 |  | √ | '0' | 是否预置数据 |
| 5 | fappkey | 服务提供者应用编码 | varchar | 36 |  | √ | ' ' | 服务提供者应用编码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffactorypackage | ServiceFactory包路径 | varchar | 100 |  | √ | ' ' | ServiceFactory包路径 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fbizcloud | 业务云 | varchar | 36 |  | √ | ' ' | 业务云 bos_devportal_bizcloud |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcloudkey | 服务提供者云编码 | varchar | 36 |  | √ | ' ' | 服务提供者云编码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fservicename | 微服务接口名 | varchar | 100 |  | √ | ' ' | 微服务接口名 |
| 15 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_cooperation_num |  | fnumber |
| 2 | idx_wf_cooperation_enable |  | fenable |
| 3 | idx_wf_cooperation_status |  | fstatus |
| 4 | t_wf_cooperationdef_pkey |  | fid |

---

## 关系类型-子表 t_wf_relationtypedef

- **表名称：** 关系类型-子表
- **表名：** t_wf_relationtypedef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freltypenum | 关系类型编码 | varchar | 36 |  | √ | ' ' | 关系类型编码 |
| 3 | freltypedesc | 描述 | varchar | 230 |  | √ | ' ' | 描述 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | freltypename | 关系类型名称 | varchar | 230 |  | √ | ' ' | 关系类型名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fapimethod | API方法名称 | varchar | 100 |  | √ | ' ' | API方法名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_relationtype_num |  | fid,freltypenum |
| 2 | t_wf_relationtypedef_pkey |  | fentryid |

---

## 工作流协作关系-多语言表 t_wf_cooperationdef_l

- **表名称：** 工作流协作关系-多语言表
- **表名：** t_wf_cooperationdef_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_cooperationdef_l |  | fid,flocaleid |
| 2 | t_wf_cooperationdef_l_pkey |  | fpkid |

---

## 方法参数-多语言表 t_wf_reltypeparamsdef_l

- **表名称：** 方法参数-多语言表
- **表名：** t_wf_reltypeparamsdef_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparamdesc | 参数描述 | varchar | 230 |  | √ | ' ' | 参数描述 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_reltypeparamsdef_l_pkey |  | fpkid |
| 2 | idx_wf_reltypeparamsdef_l |  | fdetailid,flocaleid |

---

## 关系类型-多语言表 t_wf_relationtypedef_l

- **表名称：** 关系类型-多语言表
- **表名：** t_wf_relationtypedef_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | freltypedesc | 描述 | varchar | 230 |  | √ | ' ' | 描述 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | freltypename | 关系类型名称 | varchar | 230 |  | √ | ' ' | 关系类型名称 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_relationtypedef_l_pkey |  | fpkid |
| 2 | idx_wf_relationtypedef_l |  | fentryid,flocaleid |

---

## 方法参数-子表 t_wf_reltypeparamsdef

- **表名称：** 方法参数-子表
- **表名：** t_wf_reltypeparamsdef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparamname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 2 | fparamustinput | 参数值必录 | bpchar | 1 |  | √ | '1' | 参数值必录 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fparamtype | 参数类型 | varchar | 36 |  | √ | ' ' | 参数类型,枚举: decimal :数值型 text :文本型 boolean :布尔型 datetime :日期型 entityobject :对象型 |
| 5 | fparamdesc | 参数描述 | varchar | 230 |  | √ | ' ' | 参数描述 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentityobject | 实体对象 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_reltypeparamsdef_pkey |  | fdetailid |
| 2 | idx_wf_reltypeparams_name |  | fentryid,fparamname |

---

## 参照人类型-多选基础资料表 t_wf_refpersontype

- **表名称：** 参照人类型-多选基础资料表
- **表名：** t_wf_refpersontype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 18 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_refpersontype_pkey |  | fpkid |
| 2 | idx_wf_refpersontype |  | fid |
