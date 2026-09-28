# 追溯查询方案设置-pqt_traceconfig

## 追溯查询方案设置-主表 t_pqt_traceconfig

- **表名称：** 追溯查询方案设置-主表
- **表名：** t_pqt_traceconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fenter | 下次以此方案自动进入 | bpchar | 1 |  | √ | '0' | 下次以此方案自动进入 |
| 5 | ftracetype | 追溯类型 | varchar | 50 |  | √ | ' ' | 追溯类型,枚举: LOTTRACE :批号追溯 SERIALNOTRACE :序列号追溯 COMPLEXTRACE :批号序列号综合追溯 SINGLETRACE :单品序列号追溯 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fretraceroute | 产品树追溯路径 | int8 | 64 |  | √ | 0 | [产品树追溯路径 pqt_retraceroute](../pqt_files/pqt_retraceroute.md) |
| 8 | fserial | 序列号 | int8 | 64 |  | √ | 0 | [序列号主档 bd_snmainfile](../sbd_files/bd_snmainfile.md) |
| 9 | fretracemodel | 质量追溯范围 | int8 | 64 |  | √ | 0 | [质量追溯范围 pqt_retracemodel](../pqt_files/pqt_retracemodel.md) |
| 10 | fisshowname | 产品结构树节点显示物料名称 | bpchar | 1 |  | √ | '0' | 产品结构树节点显示物料名称 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbillenddate | 单据日期.结束 | timestamp | 0 |  |  | null | 单据日期.结束 |
| 13 | fschemename | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 14 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillstartdate | 单据日期.开始 | timestamp | 0 |  |  | null | 单据日期.开始 |
| 17 | fretracelevel | 追溯层级 | int4 | 32 |  | √ | 0 | 追溯层级 |
| 18 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 19 | flot | 批号 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 20 | freworktrace | 追溯返工生产/委外工单 | bpchar | 1 |  | √ | '0' | 追溯返工生产/委外工单 |
| 21 | foprworkshop | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fisnoshow | 不显示非批号/序列号管理物料 | bpchar | 1 |  | √ | '0' | 不显示非批号/序列号管理物料 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pqt_traceconfig |  | fid |
| 2 | idx_pqt_traceconfig_fsname |  | fschemename |

---

## 查询组织-多选基础资料表 t_pqt_traceorg

- **表名称：** 查询组织-多选基础资料表
- **表名：** t_pqt_traceorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pqt_traceorg |  | fpkid |
| 2 | idx_pqt_traceorg_fid |  | fid,fbasedataid |
