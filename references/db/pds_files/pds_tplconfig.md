# 组件模板配置-pds_tplconfig

## 组件分录-子表 t_pds_tplconfigentry

- **表名称：** 组件分录-子表
- **表名：** t_pds_tplconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomponentid | 组件 | int8 | 64 |  | √ | 0 | 组件注册 pds_compreg |
| 3 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 6 | fextobject | fextobject | varchar | 50 |  | √ | ' ' |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_tplconfigentry |  | fentryid |
| 2 | idx_pds_tplconfigentry_com |  | fcomponentid |
| 3 | idx_pds_tplconfigentry_fid |  | fid |
| 4 | idx_pds_tplconfigentry_biz |  | fbizobject |

---

## 组件模板配置-多语言表 t_pds_tplconfig_l

- **表名称：** 组件模板配置-多语言表
- **表名：** t_pds_tplconfig_l

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
| 1 | pk_pds_tplconfig_l |  | fpkid |
| 2 | idx_pds_tplconfig_l_fid |  | fid,flocaleid |

---

## 组件模板配置-主表 t_pds_tplconfig

- **表名称：** 组件模板配置-主表
- **表名：** t_pds_tplconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fislatestprice | 采购清单仅显示最新报价 | bpchar | 1 |  | √ | '0' | 采购清单仅显示最新报价 |
| 3 | fbiznodeid | 应用的业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 4 | fissupplier | 供应商端模板 | bpchar | 1 |  | √ | '0' | 供应商端模板 |
| 5 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 6 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fisattachpurlist | 是否附加采购清单组件 | bpchar | 1 |  | √ | '0' | 是否附加采购清单组件 |
| 13 | fisaddpurlist | 是否创建采购清单组件 | bpchar | 1 |  | √ | '0' | 是否创建采购清单组件 |
| 14 | fopenstatus | 寻源项目开标情况 | varchar | 50 |  | √ | ' ' | 寻源项目开标情况,枚举: 1 :待开标 2 :已开技术标 3 :已开商务标 4 :已开标 5 :议价中 9 :已定标 A :已归档 B :已终止 |
| 15 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 18 | fpricebiztype | 核价业务类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 22 | fpushstatus | 签约单下推情况 | bpchar | 1 |  | √ | ' ' | 签约单下推情况,枚举: 0 :未下推 1 :已下推 |
| 23 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 24 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fshowtype | 组件展示方式 | bpchar | 1 |  | √ | ' ' | 组件展示方式,枚举: 1 :组件以页签形式展示 2 :组件以平铺形式展示 |
| 27 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_tplconfig_fsource |  | fsourcetypeid |
| 2 | pk_pds_tplconfig |  | fid |
| 3 | idx_pds_tplconfig_fnumber |  | fnumber |
| 4 | idx_pds_tplconfig_fmasterid |  | fmasterid |
| 5 | idx_pds_tplconfig_fbiznodeid |  | fbiznodeid |

---

## 寻源流程-多选基础资料表 t_pds_tplconfig_srctype

- **表名称：** 寻源流程-多选基础资料表
- **表名：** t_pds_tplconfig_srctype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_tplconfig_srctype_fid |  | fid |
| 2 | idx_pds_tplconfig_srctype_bid |  | fbasedataid |
| 3 | pk_pds_tplconfig_srctype |  | fpkid |
