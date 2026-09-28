# 归档对象-pds_fileobject

## 适用寻源方式-多选基础资料表 t_pds_filereportsrctype

- **表名称：** 适用寻源方式-多选基础资料表
- **表名：** t_pds_filereportsrctype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_filereportsrctype |  | fpkid |
| 2 | idx_pds_filereportsrctype_fid |  | fentryid |
| 3 | idx_pds_filereportsrctype_bid |  | fbasedataid |

---

## 适用寻源流程-多选基础资料表 t_pds_filereportsrcflow

- **表名称：** 适用寻源流程-多选基础资料表
- **表名：** t_pds_filereportsrcflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_filereportsrcflow_bid |  | fbasedataid |
| 2 | pk_pds_filereportsrcflow |  | fpkid |
| 3 | idx_pds_filereportsrcflow_fid |  | fentryid |

---

## 归档对象-主表 t_pds_fileobject

- **表名称：** 归档对象-主表
- **表名：** t_pds_fileobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fisv_id | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 6 | fgroupid | 归档目录 | int8 | 64 |  | √ | 0 | [归档目录 pds_filecatalogue](../pds_files/pds_filecatalogue.md) |
| 7 | fkeyfield | 关键字段 | varchar | 50 |  | √ | ' ' | 关键字段,枚举: |
| 8 | fcondition_tag | 条件对象(后台字段)_详情 | text | 0 |  |  | null | 条件对象(后台字段)_详情 |
| 9 | ffiltertype | 数据获取方式 | bpchar | 1 |  | √ | '1' | 数据获取方式,枚举: 1 :通过关键字段直接获取 2 :组件，且通过父单据关联获取 3 :通过过滤插件获取 4 :通过扩展过滤方案获取 |
| 10 | fextplugin | 扩展过滤插件 | varchar | 255 |  | √ | ' ' | 扩展过滤插件 |
| 11 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 13 | fpkeyfield | 父单据关键字段 | varchar | 50 |  | √ | ' ' | 父单据关键字段,枚举: |
| 14 | fpentitykey | 父单据实体 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fcondition | 条件对象(后台字段) | varchar | 255 |  | √ | ' ' | 条件对象(后台字段) |
| 21 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 22 | fextfilterid | 扩展过滤方案 | int8 | 64 |  | √ | 0 | [扩展过滤 pds_extfilter](../pds_files/pds_extfilter.md) |
| 23 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_fileobject_num |  | fnumber |
| 2 | idx_pds_fileobject_mid |  | fmasterid |
| 3 | pk_pds_fileobject |  | fid |

---

## 单据附件-子表 t_pds_fileobjectbill

- **表名称：** 单据附件-子表
- **表名：** t_pds_fileobjectbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fbillattach | 附件面板 | varchar | 30 |  | √ | ' ' | 附件面板,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_fileobjectbill_fid |  | fid |
| 2 | pk_pds_fileobjectbill |  | fentryid |

---

## 适用寻源方式-多选基础资料表 t_pds_filesbillsrctype

- **表名称：** 适用寻源方式-多选基础资料表
- **表名：** t_pds_filesbillsrctype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_filesbillsrctype |  | fpkid |
| 2 | idx_pds_filesbillsrctype_fid |  | fentryid |
| 3 | idx_pds_filesbillsrctype_bid |  | fbasedataid |

---

## 分录附件-子表 t_pds_fileobjectentry

- **表名称：** 分录附件-子表
- **表名：** t_pds_fileobjectentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryattach | 分录附件字段 | varchar | 30 |  | √ | ' ' | 分录附件字段,枚举: |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_fileobjectentry |  | fentryid |
| 2 | idx_pds_fileobjectentry_fid |  | fid |

---

## 归档对象-多语言表 t_pds_fileobject_l

- **表名称：** 归档对象-多语言表
- **表名：** t_pds_fileobject_l

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
| 1 | idx_pds_fileobject_l_fid |  | fid,flocaleid |
| 2 | pk_pds_fileobject_l |  | fpkid |

---

## 套打报表-子表 t_pds_fileobjectreport

- **表名称：** 套打报表-子表
- **表名：** t_pds_fileobjectreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | freportattachid | 套打模板 | varchar | 36 |  | √ | ' ' | [打印元数据 bos_print_meta](../cts_files/bos_print_meta.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_fileobjectreport_fid |  | fid |
| 2 | pk_pds_fileobjectreport |  | fentryid |

---

## 适用寻源方式-多选基础资料表 t_pds_fileentrysrctype

- **表名称：** 适用寻源方式-多选基础资料表
- **表名：** t_pds_fileentrysrctype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_fileentrysrctype_fid |  | fentryid |
| 2 | idx_pds_fileentrysrctype_bid |  | fbasedataid |
| 3 | pk_pds_fileentrysrctype |  | fpkid |

---

## 适用寻源流程-多选基础资料表 t_pds_fileentrysrcflow

- **表名称：** 适用寻源流程-多选基础资料表
- **表名：** t_pds_fileentrysrcflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_fileentrysrcflow |  | fpkid |
| 2 | idx_pds_fileentrysrcflow_fid |  | fentryid |
| 3 | idx_pds_fileentrysrcflow_bid |  | fbasedataid |

---

## 适用寻源流程-多选基础资料表 t_pds_filesbillsrcflow

- **表名称：** 适用寻源流程-多选基础资料表
- **表名：** t_pds_filesbillsrcflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_filesbillsrcflow_bid |  | fbasedataid |
| 2 | idx_pds_filesbillsrcflow_fid |  | fentryid |
| 3 | pk_pds_filesbillsrcflow |  | fpkid |
