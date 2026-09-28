# 地价抵减销项台账-tcvat_fdc_djdjxx_tz

## 地价抵减销项台账-主表 t_tcvat_fdc_djdjxx_tz

- **表名称：** 地价抵减销项台账-主表
- **表名：** t_tcvat_fdc_djdjxx_tz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fstage | 工程项目分期 | int8 | 64 |  | √ | 0 | [分期信息 bastax_stage](../bastax_files/bastax_stage.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | fdevlandinfo | 土地信息编号 | int8 | 64 |  | √ | 0 | [开发土地信息 tdm_develop_land_info](../tdm_files/tdm_develop_land_info.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 13 | fproject | 税务项目 | int8 | 64 |  | √ | 0 | [税务项目信息 bastax_taxproject](../bastax_files/bastax_taxproject.md) |
| 14 | fbillno | 台账编号 | varchar | 30 |  | √ | ' ' | 台账编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_fdc_djdjxx_tz_uni |  | forgid,fproject,fstage,fskssqq,fskssqz |
| 2 | pk_tcvat_fdc_djdjxx_tz |  | fid |

---

## 抵减土地价款详情-子表 t_tcvat_fdc_djdjxx_tz_ite

- **表名称：** 抵减土地价款详情-子表
- **表名：** t_tcvat_fdc_djdjxx_tz_ite

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdsjrksmj | fdsjrksmj | numeric | 23 | 10 | √ | 0 |  |
| 3 | fyxdjtdjkhj | （2）允许抵减土地价款合计 | numeric | 23 | 10 | √ | 0 | （2）允许抵减土地价款合计 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsykdjjrksmj | （8）剩余可抵减计容可售面积（1-3-5） | numeric | 23 | 10 | √ | 0 | （8）剩余可抵减计容可售面积（1-3-5） |
| 6 | fsykdjtdjk | （9）剩余可抵减土地价款（2-4-7） | numeric | 23 | 10 | √ | 0 | （9）剩余可抵减土地价款（2-4-7） |
| 7 | fdsjrzksmj | （1）地上计容总可售面积 | numeric | 23 | 10 | √ | 0 | （1）地上计容总可售面积 |
| 8 | fdqdjjrksmj | （5）当期抵减计容可售面积 | numeric | 23 | 10 | √ | 0 | （5）当期抵减计容可售面积 |
| 9 | fdqsjdjtdjk | （7）当期实际抵减土地价款（6） | numeric | 23 | 10 | √ | 0 | （7）当期实际抵减土地价款（6） |
| 10 | fyqqjydjdjjk | （4）以前期间已抵减土地价款（上期4+上期7） | numeric | 23 | 10 | √ | 0 | （4）以前期间已抵减土地价款（上期4+上期7） |
| 11 | fdqydjtdjk | （6）当期应抵减土地价款（(3+5)/1*2-4） | numeric | 23 | 10 | √ | 0 | （6）当期应抵减土地价款（(3+5)/1*2-4） |
| 12 | fyqqjydjjrksmj | （3）以前期间已抵减计容可售面积（上期3+上期5） | numeric | 23 | 10 | √ | 0 | （3）以前期间已抵减计容可售面积（上期3+上期5） |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_fdc_djdjxx_tz_ite |  | fentryid |
| 2 | idx_tcvat_fdc_djdjxx_tz_ite_fk |  | fid |
