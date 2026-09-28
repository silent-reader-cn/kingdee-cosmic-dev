# 追溯查询方案设置-pqt_traceconfig

## 追溯查询方案设置-主表 t_pqt_traceconfig

- **表名称：** 追溯查询方案设置-主表
- **表名：** t_pqt_traceconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fenter | 下次以此方案自动进入 | bpchar | 1 |  | √ | '0' | 下次以此方案自动进入 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fretraceroute | 产品树追溯路径 | int8 | 64 |  | √ | 0 | 产品树追溯路径 pqt_retraceroute |
| 7 | fserial | 序列号 | int8 | 64 |  | √ | 0 | 序列号主档 bd_snmainfile |
| 8 | fretracemodel | 质量追溯范围 | int8 | 64 |  | √ | 0 | 质量追溯范围 pqt_retracemodel |
| 9 | fisshowname | 产品结构树节点显示物料名称 | bpchar | 1 |  | √ | '0' | 产品结构树节点显示物料名称 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbillenddate | 单据日期.结束 | timestamp | 0 |  |  | null | 单据日期.结束 |
| 12 | fschemename | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 13 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbillstartdate | 单据日期.开始 | timestamp | 0 |  |  | null | 单据日期.开始 |
| 16 | fretracelevel | 追溯层级 | int4 | 32 |  | √ | 0 | 追溯层级 |
| 17 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 18 | flot | 批号 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 19 | foprworkshop | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fisnoshow | 不显示非批号/序列号管理物料 | bpchar | 1 |  | √ | '0' | 不显示非批号/序列号管理物料 |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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
