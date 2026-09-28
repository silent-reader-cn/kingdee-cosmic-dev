# 寻源变更(移动测试)-src_bidchange_movtest

## 采购组织(多选)-多选基础资料表 t_src_bidchange_org

- **表名称：** 采购组织(多选)-多选基础资料表
- **表名：** t_src_bidchange_org

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
| 1 | idx_src_bidchange_org_fid |  | fid |
| 2 | pk_src_bidchange_org |  | fpkid |
| 3 | idx_src_bidchange_org_bid |  | fbasedataid |

---

## 变更逻辑分录-子表 t_src_bidchange_handler

- **表名称：** 变更逻辑分录-子表
- **表名：** t_src_bidchange_handler

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fhandlerid | 变更处理逻辑 | int8 | 64 |  | √ | 0 | 变更逻辑 pds_chghandler |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_handler_fid |  | fid |
| 2 | pk_src_bidchange_handler |  | fentryid |

---

## 模板分录-子表 t_src_projecttpl

- **表名称：** 模板分录-子表
- **表名：** t_src_projecttpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomponentid | 业务组件 | int8 | 64 |  | √ | 0 | 组件注册 pds_compreg |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 4 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 5 | fsrctplid | 来源模板ID | varchar | 50 |  | √ | ' ' | 来源模板ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projecttpl_fscp |  | fsrctplid |
| 2 | idx_src_projecttpl_fobj |  | fbizobject |
| 3 | pk_src_projecttpl |  | fentryid |
| 4 | idx_src_projecttpl_fcom |  | fcomponentid |
| 5 | idx_src_projecttpl_fid |  | fid |
| 6 | idx_src_projecttpl_ftem |  | ftemplateid |

---

## 变更条件分录-子表 t_src_bidchange_condition

- **表名称：** 变更条件分录-子表
- **表名：** t_src_bidchange_condition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fconditionid | 变更判断逻辑 | int8 | 64 |  | √ | 0 | 变更条件 pds_chgcondition |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_condition_fid |  | fid |
| 2 | pk_src_bidchange_condition |  | fentryid |

---

## 单据体-子表 t_src_bidchange_log

- **表名称：** 单据体-子表
- **表名：** t_src_bidchange_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fchgcontent | 变更内容 | varchar | 510 |  | √ | ' ' | 变更内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_bidchange_log_fid |  | fid |
| 2 | pk_src_bidchange_log |  | fentryid |

---

## 寻源变更(移动测试)-主表 t_src_bidchange

- **表名称：** 寻源变更(移动测试)-主表
- **表名：** t_src_bidchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbilldate | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 4 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fapplyid | 寻源申请 | int8 | 64 |  | √ | 0 | 寻源申请F7 src_applyf7 |
| 8 | fdemandid | 项目 | int8 | 64 |  | √ | 0 | 项目立项查询 src_demandno |
| 9 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 10 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 11 | fpurdecision | 采购决策（是否上采委会） | bpchar | 1 |  | √ | ' ' | 采购决策（是否上采委会） |
| 12 | fbillno | 变更单号 | varchar | 30 |  | √ | ' ' | 变更单号 |
| 13 | fremark | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | ftemplateid | 变更类型 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 16 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fdescription | 变更摘要 | varchar | 1020 |  | √ | ' ' | 变更摘要 |
| 23 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 24 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 25 | fisdemandpush | 是否项目立项下推 | bpchar | 1 |  | √ | '0' | 是否项目立项下推 |
| 26 | flevel | 采会会层级 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 27 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 28 | fissuabnormal | 是否供应商数量异常 | bpchar | 1 |  | √ | '0' | 是否供应商数量异常 |
| 29 | fchangesource | 变更来源 | bpchar | 1 |  | √ | '3' | 变更来源,枚举: 2 :项目立项 3 :招标项目 |
| 30 | fcurrentnode | 变更时当前节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_bidchange_fprojectid |  | fprojectid |
| 2 | idx_src_bidchange_ftemplateid |  | ftemplateid |
| 3 | idx_src_bidchange_fparentid |  | fparentid |
| 4 | pk_src_bidchange |  | fid |
| 5 | idx_src_bidchange_fbillno |  | fbillno |
| 6 | idx_src_bidchange_fbilldate |  | fbilldate |

---

## 供应商用户-多选基础资料表 t_src_supplieruser

- **表名称：** 供应商用户-多选基础资料表
- **表名：** t_src_supplieruser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supplieruser_bid |  | fbasedataid |
| 2 | pk_src_supplieruser |  | fpkid |
| 3 | idx_src_supplieruser_fid |  | fid |
