# 费用分配标准-sco_costdriver

## 资源-多选基础资料表 t_sco_costdriver_resource

- **表名称：** 资源-多选基础资料表
- **表名：** t_sco_costdriver_resource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costdriver_resource |  | fpkid |
| 2 | idx_sco_costdriver_resource |  | fid,fpkid |

---

## 费用分配标准-主表 t_sco_costdriver

- **表名称：** 费用分配标准-主表
- **表名：** t_sco_costdriver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmatchpattern | 匹配模式 | varchar | 30 |  | √ | 'resource' | 匹配模式,枚举: resource :资源 resourcetype :资源类型 |
| 3 | fsubelementid | fsubelementid | int8 | 64 |  | √ | 0 |  |
| 4 | fworkactivityid | 作业活动 | int8 | 64 |  | √ | 0 | [作业活动 sco_new_workactivity](../sco_files/sco_new_workactivity.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sco :标准成本 |
| 7 | fislinkresource | 关联资源 | bpchar | 1 |  | √ | '0' | 关联资源 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fformulastr | 公式设置 | varchar | 255 |  | √ | ' ' | 公式设置 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fformula | 公式设置 | varchar | 510 |  | √ | ' ' | 公式设置 |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | felementid | felementid | int8 | 64 |  | √ | 0 |  |
| 25 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | fallocclass | 分配层级 | varchar | 30 |  | √ | ' ' | 分配层级,枚举: COSTCENTER :成本中心 MATERIAL :物料 COSTOBJECT :成本核算对象 MATERIALGROUP :物料分类 |
| 27 | fismatgroupcal | 物料分类分级计算 | bpchar | 1 |  | √ | '0' | 物料分类分级计算 |
| 28 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 29 | fresourcetype | 资源类型 | bpchar | 100 |  | √ | '0' | 资源类型,枚举: A :设备 B :人员 C :工装资源 D :模具资源 E :制造人员 |
| 30 | fiscomplexcd | 复合分配标准 | bpchar | 1 |  | √ | '0' | 复合分配标准 |
| 31 | fmatchreport | 匹配资源耗用量归集单 | varchar | 30 |  | √ | 'total' | 匹配资源耗用量归集单,枚举: total :实际工时 much :实际用量 |
| 32 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 33 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 35 | fisrelatedwork | 关联作业 | bpchar | 1 |  | √ | '0' | 关联作业 |
| 36 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costdriver |  | fid |
| 2 | idx_t_sco_costdriver_master |  | fmasterid |
| 3 | index_sco_costdriver |  | fmasterid |
| 4 | idx_t_sco_costdriver_createorg |  | fcreateorgid |

---

## 费用分配标准-多语言表 t_sco_costdriver_l

- **表名称：** 费用分配标准-多语言表
- **表名：** t_sco_costdriver_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sco_costdriver_l |  | fid,flocaleid |
| 2 | pk_sco_costdriver_l |  | fpkid |

---

## 费用分配标准-使用范围表 t_sco_costdriver_u

- **表名称：** 费用分配标准-使用范围表
- **表名：** t_sco_costdriver_u

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
| 1 | idx_t_sco_costdriver_u_uo |  | fuseorgid |
| 2 | pk_t_sco_costdriver_u |  | fdataid,fuseorgid |
