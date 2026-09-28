# 发布调查表-srm_sendquestion

## 发布调查表-主表 t_srm_sendquestion

- **表名称：** 发布调查表-主表
- **表名：** t_srm_sendquestion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 说明 | varchar | 2000 |  | √ | ' ' | 说明 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 发布组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fquestionsconfigid | 调查表模板 | int8 | 64 |  | √ | 0 | [调查表模板配置 pbd_questionconfig](../pbd_files/pbd_questionconfig.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbizdate | 发布日期 | timestamp | 0 |  |  | null | 发布日期 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_sendquestion |  | fid |
| 2 | idx_srm_sendquestion_fbillno |  | fbillno |

---

## 供应商分录-子表 t_srm_sendquestion_sup

- **表名称：** 供应商分录-子表
- **表名：** t_srm_sendquestion_sup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpuruserid | 供应商用户 | int8 | 64 |  | √ | 0 | [供应商用户 pur_supuser](../basedata_files/pur_supuser.md) |
| 3 | fbdsupplierno | 主数据供应商编码 | varchar | 50 |  | √ | ' ' | 主数据供应商编码 |
| 4 | fuserphone | 手机号 | varchar | 80 |  | √ | ' ' | 手机号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fuseremail | 邮箱 | varchar | 80 |  | √ | ' ' | 邮箱 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsupplierid | 供应商名称 | int8 | 64 |  | √ | 0 | [供应商 srm_supplier](../srm_files/srm_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_sendquestion_sup |  | fentryid |
| 2 | idx_srm_sendquestion_sup_fid |  | fid |
