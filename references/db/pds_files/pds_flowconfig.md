# 流程配置-pds_flowconfig

## 品类-多选基础资料表 t_pds_flowcategory

- **表名称：** 品类-多选基础资料表
- **表名：** t_pds_flowcategory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_flowcategory |  | fpkid |
| 2 | idx_pds_flowcategory_fid |  | fid |
| 3 | idx_pds_flowcategory_bid |  | fbasedataid |

---

## 采购组织-多选基础资料表 t_pds_flowpurorg

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_pds_flowpurorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_flowpurorg_bid |  | fbasedataid |
| 2 | pk_pds_flowpurorg |  | fpkid |
| 3 | idx_pds_flowpurorg_fid |  | fid |

---

## 参数分录-子表 t_pds_flowparams

- **表名称：** 参数分录-子表
- **表名：** t_pds_flowparams

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamvalue | 默认值 | varchar | 512 |  | √ | ' ' | 默认值 |
| 3 | fparameterid | 参数编码 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 4 | fparamname | fparamname | varchar | 50 |  | √ | ' ' |  |
| 5 | fbasedatainfo | 参数说明 | varchar | 512 |  | √ | ' ' | 参数说明 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fismust | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 8 | fparamtype | fparamtype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_flowparams |  | fentryid |
| 2 | idx_pds_flowparams_fid |  | fid |

---

## 采购组-多选基础资料表 t_pds_flowpurgroup

- **表名称：** 采购组-多选基础资料表
- **表名：** t_pds_flowpurgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购业务组(封存) bd_pmoperatorgroup |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_flowpurgroup_bid |  | fbasedataid |
| 2 | pk_pds_flowpurgroup |  | fpkid |
| 3 | idx_pds_flowpurgroup_fid |  | fid |

---

## 流程节点分录-子表 t_pds_flownode

- **表名称：** 流程节点分录-子表
- **表名：** t_pds_flownode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbiznodeid | 关键业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 4 | fnodename | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 5 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 6 | fneedaudit | 是否需要审核 | bpchar | 1 |  | √ | ' ' | 是否需要审核 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 9 | fextobject | 对应状态表 | varchar | 50 |  | √ | ' ' | 对应状态表 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fisflowchart | 是否在流程图显示 | bpchar | 1 |  | √ | '0' | 是否在流程图显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_node_fid |  | fid |
| 2 | pk_pds_flownode |  | fentryid |
| 3 | idx_pds_node_fbiznodeid |  | fbiznodeid |
| 4 | idx_pds_node_fbizobject |  | fbizobject |
| 5 | idx_pds_node_fextobject |  | fextobject |

---

## 并行节点分录-子表 t_pds_flownodesub

- **表名称：** 并行节点分录-子表
- **表名：** t_pds_flownodesub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbiznodeid | 附属业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 2 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 3 | fnodename | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 4 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 7 | fextobject | 对应状态表 | varchar | 50 |  | √ | ' ' | 对应状态表 |
| 8 | fisaudit | 是否需要审核 | bpchar | 1 |  | √ | '0' | 是否需要审核 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fisflowchart | 是否在流程图显示 | bpchar | 1 |  | √ | '0' | 是否在流程图显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_sub_fbizobject |  | fbizobject |
| 2 | idx_pds_sub_fentryid |  | fentryid |
| 3 | pk_pds_flownodesub |  | fdetailid |
| 4 | idx_pds_sub_fextobject |  | fextobject |
| 5 | idx_pds_sub_fbiznodeid |  | fbiznodeid |

---

## 流程配置-主表 t_pds_flowconfig

- **表名称：** 流程配置-主表
- **表名：** t_pds_flowconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissupplier | 供应商端流程 | bpchar | 1 |  | √ | '0' | 供应商端流程 |
| 3 | fismanualscore | 手工录入商务得分 | bpchar | 1 |  | √ | '0' | 手工录入商务得分 |
| 4 | fminisuppliers | 最低邀请供应商数量 | int4 | 32 |  | √ | 0 | 最低邀请供应商数量 |
| 5 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 6 | ftieredtype | 阶梯报价方式 | bpchar | 1 |  | √ | '1' | 阶梯报价方式,枚举: 1 :不启用阶梯报价 2 :采购清单分录阶梯报价 3 :采购清单子表阶梯报价 |
| 7 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 8 | fisnegotiable | 定标后允许再议价(暂不支持) | bpchar | 1 |  | √ | '0' | 定标后允许再议价(暂不支持) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 12 | fisneedbiddoc | 采购方是否必须上传标书 | bpchar | 1 |  | √ | '0' | 采购方是否必须上传标书 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | finvitenodeid | 发邀请函的业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 16 | fopentype | 开标方式(开标顺序) | bpchar | 1 |  | √ | ' ' | 开标方式(开标顺序),枚举: 1 :同时开技术标和商务标 2 :先开评技术标，后开商务标 9 :报价即开标(非密封报价) 4 :并行开技术标和商务标 |
| 17 | fisneednotice | 公开招标发布公告后才允许供应商报名 | bpchar | 1 |  | √ | '0' | 公开招标发布公告后才允许供应商报名 |
| 18 | ftendertype | 招标方式 | bpchar | 1 |  | √ | ' ' | 招标方式,枚举: 1 :邀请招标 2 :公开招标 |
| 19 | fsourceclassid | 招标方式类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 20 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 21 | fmanagetype | 管理方式 | bpchar | 1 |  | √ | '1' | 管理方式,枚举: 1 :按项目 2 :按标段 3 :按标的 |
| 22 | fisdecisionresult | 定标需关联会议决策 | bpchar | 1 |  | √ | '0' | 定标需关联会议决策 |
| 23 | fremark | 备注 | varchar | 600 |  | √ | ' ' | 备注 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fname | 流程名称 | varchar | 300 |  | √ | ' ' | 流程名称 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fchassistypeid | 底盘类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 28 | fisauditscore | 自动审核 开标与评标 节点 | bpchar | 1 |  | √ | '0' | 自动审核 开标与评标 节点 |
| 29 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | ftendency | 报价趋势 | varchar | 50 |  | √ | ' ' | 报价趋势,枚举: 1 :只允许降价 2 :只允许加价 3 :允许加价或降价 |
| 31 | fdescription | 应用场景 | varchar | 510 |  | √ | ' ' | 应用场景 |
| 32 | fbiddoc | 需要上传的标书类型 | varchar | 30 |  | √ | ' ' | 需要上传的标书类型,枚举: 1 :技术标书 2 :商务标书 3 :通用标书 4 :商务综合标书 |
| 33 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 34 | fischgmaterial | 定标后允许修改/补充物料 | bpchar | 1 |  | √ | '0' | 定标后允许修改/补充物料 |
| 35 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 36 | fissourcesupplier | 自动取货源清单供应商 | bpchar | 1 |  | √ | '0' | 自动取货源清单供应商 |
| 37 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 流程编码 | varchar | 30 |  | √ | ' ' | 流程编码 |
| 39 | fisneedinvite | 需要发送邀请函 | bpchar | 1 |  | √ | '0' | 需要发送邀请函 |
| 40 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |
| 41 | fisbizscore | 需要专家评商务分 | bpchar | 1 |  | √ | '0' | 需要专家评商务分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_flow_fnumber |  | fnumber |
| 2 | pk_pds_flowconfig |  | fid |
| 3 | idx_pds_flow_masterid |  | fmasterid |
| 4 | idx_pds_flow_fsource |  | fsourceclassid |
| 5 | idx_pds_flow_fcreatetime |  | fcreatetime |
| 6 | idx_pds_flow_fsourcetype |  | fsourcetypeid |
| 7 | idx_pds_flow_fpurdeptid |  | fpurdeptid |

---

## 业务类型-多选基础资料表 t_pds_flow_biztype

- **表名称：** 业务类型-多选基础资料表
- **表名：** t_pds_flow_biztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pds_flow_biztype_fid |  | fid |
| 2 | pk_pds_flow_biztype |  | fpkid |
| 3 | idx_t_pds_flow_biztype_bid |  | fbasedataid |

---

## 流程配置-多语言表 t_pds_flowconfig_l

- **表名称：** 流程配置-多语言表
- **表名：** t_pds_flowconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 600 |  | √ | ' ' | 备注 |
| 3 | fname | 流程名称 | varchar | 300 |  | √ | ' ' | 流程名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_srctype_l_fid |  | fid,flocaleid |
| 2 | pk_pds_flowconfig_l |  | fpkid |
| 3 | idx_pds_srctype_l_fname |  | fname |
