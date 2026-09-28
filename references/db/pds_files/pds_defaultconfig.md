# 默认值设置-pds_defaultconfig

## 招标流程-多选基础资料表 t_pds_defaultsourceflow

- **表名称：** 招标流程-多选基础资料表
- **表名：** t_pds_defaultsourceflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_defaultsourceflow_bid |  | fbasedataid |
| 2 | pk_pds_defaultsourceflow |  | fpkid |
| 3 | idx_pds_defaultsourceflow_fid |  | fid |

---

## 字段分录-多语言表 t_pds_defaultconfigentry_l

- **表名称：** 字段分录-多语言表
- **表名：** t_pds_defaultconfigentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdefaultvalue | fdefaultvalue | varchar | 300 |  | √ | ' ' |  |
| 2 | fnote | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_defaultconfigentry_eid |  | fentryid |
| 2 | pk_pds_defaultconfigentry_l |  | fpkid |

---

## 默认值设置-主表 t_pds_defaultconfig

- **表名称：** 默认值设置-主表
- **表名：** t_pds_defaultconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 4 | fbiznodeid | 业务节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcomponentid | 业务组件 | int8 | 64 |  | √ | 0 | [组件注册 pds_compreg](../pds_files/pds_compreg.md) |
| 10 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 11 | fbiztype | 公告类型 | bpchar | 1 |  | √ | ' ' | 公告类型,枚举: 1 :询价公告 2 :招标公告 3 :竞价公告 4 :比价公告 6 :招募公告 7 :行业动态 8 :系统公告 A :询价结果公告 B :竞价结果公告 C :寻源公告 5 :中标公告 D :流标公告 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fplugin | 自定义处理默认值插件 | varchar | 100 |  | √ | ' ' | 自定义处理默认值插件 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fsourceclassid | 招标方式类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 18 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_defaultconfig_cid |  | fcomponentid |
| 2 | idx_pds_defaultconfig_number |  | fnumber |
| 3 | idx_pds_defaultconfig_bid |  | fbiznodeid |
| 4 | pk_pds_defaultconfig |  | fid |

---

## 寻源方式-多选基础资料表 t_pds_defaultsourcetype

- **表名称：** 寻源方式-多选基础资料表
- **表名：** t_pds_defaultsourcetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_defaultsourcetype |  | fpkid |
| 2 | idx_pds_defaultsourcetype_fid |  | fid |
| 3 | idx_pds_defaultsourcetype_bid |  | fbasedataid |

---

## 默认值设置-多语言表 t_pds_defaultconfig_l

- **表名称：** 默认值设置-多语言表
- **表名：** t_pds_defaultconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_defaultconfig_l_fid |  | fid |
| 2 | pk_pds_defaultconfig_l |  | fpkid |

---

## 字段分录-子表 t_pds_defaultconfigentry

- **表名称：** 字段分录-子表
- **表名：** t_pds_defaultconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称,枚举: |
| 3 | fdefaultvalue | 默认值 | varchar | 300 |  | √ | ' ' | 默认值 |
| 4 | fbasedatainfo | 基础资料详情 | varchar | 512 |  | √ | ' ' | 基础资料详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fparamtype | 参数类型 | bpchar | 1 |  | √ | ' ' | 参数类型,枚举: 0 :文本 1 :整数 2 :长整数 3 :小数 4 :日期 5 :长日期 6 :时间 7 :布尔类型 8 :基础资料 9 :下拉选 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ffieldid | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_defaultconfigentry |  | fentryid |
| 2 | idx_pds_defaultconfigentry_fid |  | fid |
