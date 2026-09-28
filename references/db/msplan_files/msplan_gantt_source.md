# 甘特图数据源-msplan_gantt_source

## 横道类型标签设置-子表 t_msplan_crosscontent

- **表名称：** 横道类型标签设置-子表
- **表名：** t_msplan_crosscontent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flabelformat | flabelformat | varchar | 50 |  | √ | ' ' |  |
| 2 | fentryflagdetailconnector | fentryflagdetailconnector | varchar | 50 |  | √ | ' ' |  |
| 3 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 4 | fcsviewschemeid | fcsviewschemeid | varchar | 255 |  | √ | 0 |  |
| 5 | fentrycrossfcdescone | fentrycrossfcdescone | varchar | 2000 |  | √ | ' ' |  |
| 6 | fltypeone | fltypeone | varchar | 50 |  | √ | ' ' |  |
| 7 | fcviewid | fcviewid | int8 | 64 |  | √ | 0 |  |
| 8 | fentrycrossflagcontentdes | fentrycrossflagcontentdes | varchar | 2000 |  | √ | ' ' |  |
| 9 | flabeltypeone | flabeltypeone | varchar | 5 |  | √ | ' ' |  |
| 10 | fentryflagconnector | fentryflagconnector | varchar | 50 |  | √ | ' ' |  |
| 11 | flabeltype | flabeltype | varchar | 5 |  | √ | ' ' |  |
| 12 | fltypeonewo | fltypeonewo | varchar | 50 |  | √ | ' ' |  |
| 13 | fentrycrossflagcontent | fentrycrossflagcontent | varchar | 2000 |  | √ | ' ' |  |
| 14 | fentrycrossfcone | fentrycrossfcone | varchar | 2000 |  | √ | ' ' |  |
| 15 | flabelformattwo | flabelformattwo | varchar | 50 |  | √ | ' ' |  |
| 16 | fcviewalias | fcviewalias | varchar | 50 |  | √ | ' ' |  |
| 17 | flabelformatone | flabelformatone | varchar | 50 |  | √ | ' ' |  |
| 18 | flabeltypetwo | flabeltypetwo | varchar | 50 |  | √ | ' ' |  |
| 19 | fentrycrossflagdetaildesc | fentrycrossflagdetaildesc | varchar | 2000 |  | √ | ' ' |  |
| 20 | fltype | fltype | varchar | 50 |  | √ | ' ' |  |
| 21 | fentryflagconnectorone | fentryflagconnectorone | varchar | 50 |  | √ | ' ' |  |
| 22 | fentrycrossflagdetailcont | fentrycrossflagdetailcont | varchar | 2000 |  | √ | ' ' |  |
| 23 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_crosscontent_feq |  | fentryid,fseq |
| 2 | pk_msplan_crosscontent |  | fdetailid |

---

## 横道颜色分组-子表 t_msplan_person_color

- **表名称：** 横道颜色分组-子表
- **表名：** t_msplan_person_color

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcolorcondfilter | fcolorcondfilter | varchar | 255 |  | √ | ' ' |  |
| 3 | fcolorcondfilter_tag | fcolorcondfilter_tag | text | 0 |  |  | null |  |
| 4 | fcolorconditon | fcolorconditon | varchar | 1000 |  | √ | ' ' |  |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fcolorvalue | fcolorvalue | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_person_color |  | fid,fseq |
| 2 | pk_t_msplan_person_color |  | fentryid |

---

## 字段设置-子表 t_msplan_fentryety

- **表名称：** 字段设置-子表
- **表名：** t_msplan_fentryety

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryfieldflag | fentryfieldflag | varchar | 50 |  | √ | ' ' |  |
| 3 | fentryfieldname | fentryfieldname | varchar | 50 |  | √ | ' ' |  |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fentryfieldalign | fentryfieldalign | varchar | 50 |  | √ | ' ' |  |
| 7 | fentryentityname | fentryentityname | varchar | 255 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_fentty_fseq |  | fseq |
| 2 | idx_msplan_fentty_fid |  | fid |
| 3 | pk_msplan_fentryety |  | fentryid |

---

## 样式方案-多选基础资料表 t_msplan_souceviewscheme

- **表名称：** 样式方案-多选基础资料表
- **表名：** t_msplan_souceviewscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_soucme_fid |  | fid,fbasedataid |
| 2 | pk_msplan_souceviewscheme |  | fpkid |

---

## 横道高亮配置-子表 t_msplan_highligthcolor

- **表名称：** 横道高亮配置-子表
- **表名：** t_msplan_highligthcolor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryhighlightgpflag | fentryhighlightgpflag | varchar | 200 |  | √ | ' ' |  |
| 3 | fentryhighcolorvalue | fentryhighcolorvalue | varchar | 50 |  | √ | ' ' |  |
| 4 | fentryhighlightgroup | fentryhighlightgroup | varchar | 200 |  | √ | ' ' |  |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_highligthcl_fseq |  | fid,fseq |
| 2 | pk_msplan_highligthcolor |  | fentryid |

---

## 分组字段-子表 t_msplan_sourcegroup

- **表名称：** 分组字段-子表
- **表名：** t_msplan_sourcegroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 3 | fgrouplevel | fgrouplevel | int4 | 32 |  | √ | 0 |  |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fgroupentityflagid | fgroupentityflagid | varchar | 255 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_sourup_fseq |  | fseq |
| 2 | idx_msplan_sourup_fid |  | fid |
| 3 | pk_msplan_sourcegroup |  | fentryid |

---

## 横道图标设置-子表 t_msplan_crossiconset

- **表名称：** 横道图标设置-子表
- **表名：** t_msplan_crossiconset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaskpop | ftaskpop | varchar | 200 |  | √ | ' ' |  |
| 2 | fpictureurl | fpictureurl | varchar | 255 |  | √ | ' ' |  |
| 3 | ftaskpropvalue | ftaskpropvalue | varchar | 200 |  | √ | ' ' |  |
| 4 | ficonurl | ficonurl | varchar | 500 |  | √ | ' ' |  |
| 5 | ficonconditionvalue | ficonconditionvalue | varchar | 255 |  | √ | ' ' |  |
| 6 | ficonconditionvalue_tag | ficonconditionvalue_tag | text | 0 |  |  | null |  |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | ftaskpopfiled | ftaskpopfiled | varchar | 50 |  | √ | ' ' |  |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 10 | ftaskpropname | ftaskpropname | varchar | 50 |  | √ | ' ' |  |
| 11 | ficoncondition | ficoncondition | varchar | 200 |  | √ | ' ' |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_crossiconset_fseq |  | fentryid,fseq |
| 2 | pk_msplan_crossiconset |  | fdetailid |

---

## 横道移动控制-子表 t_msplan_crossmoveentry

- **表名称：** 横道移动控制-子表
- **表名：** t_msplan_crossmoveentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftviewalias | ftviewalias | varchar | 50 |  | √ | ' ' |  |
| 2 | ftviewid | ftviewid | int8 | 64 |  | √ | 0 |  |
| 3 | fpartmove | fpartmove | bpchar | 1 |  | √ | '0' |  |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 6 | fcmviewschemeid | fcmviewschemeid | varchar | 255 |  | √ | 0 |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fentiretymove | fentiretymove | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_crossmoveentry_feq |  | fentryid,fseq |
| 2 | pk_msplan_crossmoveentry |  | fdetailid |

---

## 实体详细设置-子表 t_msplan_entity_condition

- **表名称：** 实体详细设置-子表
- **表名：** t_msplan_entity_condition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fversionfiled | fversionfiled | varchar | 50 |  | √ | ' ' |  |
| 2 | fcentityid | fcentityid | varchar | 255 |  | √ | ' ' |  |
| 3 | fcfiltertext | fcfiltertext | varchar | 1000 |  | √ | ' ' |  |
| 4 | ffieldsort | ffieldsort | varchar | 50 |  | √ | ' ' |  |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | ffieldsortflag | ffieldsortflag | varchar | 50 |  | √ | ' ' |  |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 8 | fcfilter | fcfilter | varchar | 255 |  | √ | ' ' |  |
| 9 | fcfilter_tag | fcfilter_tag | text | 0 |  |  | null |  |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_entity_cond_fs |  | fentryid,fseq |
| 2 | pk_msplan_entity_condition |  | fdetailid |

---

## 视图方案-子表 t_msplan_entity

- **表名称：** 视图方案-子表
- **表名：** t_msplan_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaskentityflagdesc | ftaskentityflagdesc | varchar | 255 |  | √ | ' ' |  |
| 3 | fgroupentityid | fgroupentityid | varchar | 255 |  | √ | 0 |  |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fdefaultview | fdefaultview | bpchar | 1 |  | √ | '0' |  |
| 6 | fjoinfilter | fjoinfilter | bpchar | 1 |  | √ | '0' |  |
| 7 | fgroupfielddesc | fgroupfielddesc | varchar | 50 |  | √ | ' ' |  |
| 8 | ffiltertext | ffiltertext | varchar | 50 |  | √ | ' ' |  |
| 9 | ffilter | ffilter | varchar | 255 |  | √ | ' ' |  |
| 10 | fentityid | fentityid | varchar | 255 |  | √ | 0 |  |
| 11 | ftimefielddesc | ftimefielddesc | varchar | 50 |  | √ | ' ' |  |
| 12 | fupgroupfield | fupgroupfield | varchar | 50 |  | √ | ' ' |  |
| 13 | fupupgroupfield | fupupgroupfield | varchar | 50 |  | √ | ' ' |  |
| 14 | ftaskentityflag | ftaskentityflag | varchar | 255 |  | √ | ' ' |  |
| 15 | fupgroupfielddesc | fupgroupfielddesc | varchar | 50 |  | √ | ' ' |  |
| 16 | fviewid | fviewid | int8 | 64 |  | √ | 0 |  |
| 17 | ffilter_tag | ffilter_tag | text | 0 |  |  | '' |  |
| 18 | fgroupfield | fgroupfield | varchar | 50 |  | √ | ' ' |  |
| 19 | fupupgroupentityid | fupupgroupentityid | varchar | 255 |  | √ | 0 |  |
| 20 | fupupgroupfielddesc | fupupgroupfielddesc | varchar | 50 |  | √ | ' ' |  |
| 21 | ftimefield | ftimefield | varchar | 50 |  | √ | ' ' |  |
| 22 | fismappingentity | fismappingentity | bpchar | 1 |  | √ | '0' |  |
| 23 | fupgroupentityid | fupgroupentityid | varchar | 255 |  | √ | 0 |  |
| 24 | fviewalias | fviewalias | varchar | 50 |  | √ | ' ' |  |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 26 | fgantttype | fgantttype | varchar | 5 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_entity_fseq |  | fseq |
| 2 | idx_msplan_entity_fid |  | fid |
| 3 | pk_msplan_entity |  | fentryid |

---

## 过滤条件关联实体-子表 t_msplan_filterentry

- **表名称：** 过滤条件关联实体-子表
- **表名：** t_msplan_filterentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftofilterflagdesc | ftofilterflagdesc | varchar | 50 |  | √ | ' ' |  |
| 2 | ftofilterflag | ftofilterflag | varchar | 50 |  | √ | ' ' |  |
| 3 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fchildentityflag | fchildentityflag | varchar | 255 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_filtry_fentryid |  | fentryid |
| 2 | idx_msplan_filtry_fseq |  | fseq |
| 3 | pk_msplan_filterentry |  | fdetailid |

---

## 字段设置-多语言表 t_msplan_fentryety_l

- **表名称：** 字段设置-多语言表
- **表名：** t_msplan_fentryety_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' |  |
| 2 | fpkid | fpkid | varchar | 255 |  | √ | ' ' |  |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fentryfieldalign | fentryfieldalign | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_fentryety_l |  | fpkid |
| 2 | idx_msplan_fentryety_l |  | fentryid,flocaleid |

---

## 实体关系设置-子表 t_msplan_entity_relation

- **表名称：** 实体关系设置-子表
- **表名：** t_msplan_entity_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 2 | frentityflag | frentityflag | varchar | 50 |  | √ | ' ' |  |
| 3 | frentityflagdesc | frentityflagdesc | varchar | 50 |  | √ | ' ' |  |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 5 | frentityid | frentityid | varchar | 255 |  | √ | 0 |  |
| 6 | frentryflag | frentryflag | varchar | 50 |  | √ | ' ' |  |
| 7 | fruplevelentityid | fruplevelentityid | varchar | 255 |  | √ | 0 |  |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_entity_relation |  | fdetailid |
| 2 | idx_msplan_entity_relation_feq |  | fentryid,fseq |

---

## 横道对象配置-子表 t_msplan_crossset

- **表名称：** 横道对象配置-子表
- **表名：** t_msplan_crossset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcrossentityid | fcrossentityid | varchar | 255 |  | √ | 0 |  |
| 3 | fcrossflagdetaildesc | fcrossflagdetaildesc | varchar | 2000 |  | √ | ' ' |  |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fflagconnector | fflagconnector | varchar | 50 |  | √ | ' ' |  |
| 6 | fcrossflagcontent | fcrossflagcontent | varchar | 2000 |  | √ | ' ' |  |
| 7 | fcrossflagcontentdesc | fcrossflagcontentdesc | varchar | 2000 |  | √ | ' ' |  |
| 8 | fcrossflagdetailcontent | fcrossflagdetailcontent | varchar | 2000 |  | √ | ' ' |  |
| 9 | fenddatefiled | fenddatefiled | varchar | 50 |  | √ | ' ' |  |
| 10 | fcrossobj | fcrossobj | varchar | 5 |  | √ | ' ' |  |
| 11 | fstartdatefileddesc | fstartdatefileddesc | varchar | 50 |  | √ | ' ' |  |
| 12 | fcrossfcdescone | fcrossfcdescone | varchar | 2000 |  | √ | ' ' |  |
| 13 | fcrosstypeid | fcrosstypeid | int8 | 64 |  | √ | 0 |  |
| 14 | fflagdetailconnector | fflagdetailconnector | varchar | 50 |  | √ | ' ' |  |
| 15 | fisgroupcount | fisgroupcount | bpchar | 1 |  | √ | '0' |  |
| 16 | fcrossfcone | fcrossfcone | varchar | 2000 |  | √ | ' ' |  |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fstartdatefiled | fstartdatefiled | varchar | 50 |  | √ | ' ' |  |
| 19 | flandmarksfiled | flandmarksfiled | varchar | 50 |  | √ | ' ' |  |
| 20 | fenddatefileddesc | fenddatefileddesc | varchar | 50 |  | √ | ' ' |  |
| 21 | fflagconnectorone | fflagconnectorone | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_croset_fseq |  | fseq |
| 2 | idx_msplan_croset_fid |  | fid |
| 3 | pk_msplan_crossset |  | fentryid |

---

## 甘特图数据源-主表 t_msplan_gttsource

- **表名称：** 甘特图数据源-主表
- **表名：** t_msplan_gttsource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpostralationflag | fpostralationflag | varchar | 50 |  | √ | ' ' |  |
| 3 | fpreentity | fpreentity | varchar | 50 |  | √ | ' ' |  |
| 4 | fttimefield | fttimefield | varchar | 50 |  | √ | ' ' |  |
| 5 | ftaskentityid | ftaskentityid | varchar | 255 |  | √ | ' ' |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fpostralation | fpostralation | varchar | 50 |  | √ | ' ' |  |
| 8 | fpreralation | fpreralation | varchar | 50 |  | √ | ' ' |  |
| 9 | fstatus | fstatus | varchar | 1 |  | √ | ' ' |  |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | fhighlightgroup | fhighlightgroup | varchar | 50 |  | √ | ' ' |  |
| 13 | fhighlightgroupflag | fhighlightgroupflag | varchar | 50 |  | √ | ' ' |  |
| 14 | fentitylayoutid | fentitylayoutid | varchar | 255 |  | √ | ' ' |  |
| 15 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | fpreralationname | fpreralationname | varchar | 50 |  | √ | ' ' |  |
| 18 | fralationentityid | fralationentityid | varchar | 255 |  | √ | 0 |  |
| 19 | fttimefielddesc | fttimefielddesc | varchar | 50 |  | √ | ' ' |  |
| 20 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 21 | fpostentity | fpostentity | varchar | 50 |  | √ | ' ' |  |
| 22 | fgtentityid | fgtentityid | varchar | 255 |  | √ | 0 |  |
| 23 | fhighcolorvalue | fhighcolorvalue | varchar | 50 |  | √ | ' ' |  |
| 24 | fenable | fenable | varchar | 1 |  | √ | ' ' |  |
| 25 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 26 | fpostralationname | fpostralationname | varchar | 50 |  | √ | ' ' |  |
| 27 | fdatamodelmutl | fdatamodelmutl | bpchar | 1 |  | √ | '0' |  |
| 28 | fpreralationflag | fpreralationflag | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_gtsource |  | fid |
| 2 | idx_msplan_gtt_fcreatetime |  | fcreatetime |
| 3 | idx_msplan_gtt_fnumber |  | fnumber |

---

## 甘特图数据源-多语言表 t_msplan_gttsource_l

- **表名称：** 甘特图数据源-多语言表
- **表名：** t_msplan_gttsource_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 195 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' |  |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_gttl_fname |  | fname |
| 2 | pk_msplan_gtt_source_l |  | fpkid |
| 3 | idx_msplan_gttl_fid |  | fid,flocaleid |

---

## 快速定义设置-子表 t_msplan_quick_dfiled

- **表名称：** 快速定义设置-子表
- **表名：** t_msplan_quick_dfiled

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequireditem | frequireditem | bpchar | 1 |  | √ | '0' |  |
| 3 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 4 | ffieldflag | ffieldflag | varchar | 50 |  | √ | ' ' |  |
| 5 | fhidecol | fhidecol | bpchar | 1 |  | √ | '0' |  |
| 6 | ffieldname | ffieldname | varchar | 50 |  | √ | ' ' |  |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | ffiledid | ffiledid | varchar | 50 |  | √ | ' ' |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | frefbasefieldid | frefbasefieldid | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msplan_quick_dfiled |  | fentryid |
| 2 | idx_msplan_quick_dfiled |  | fid,fseq |

---

## 数据过滤设置-子表 t_msplan_filter

- **表名称：** 数据过滤设置-子表
- **表名：** t_msplan_filter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentitycondfilter | fentitycondfilter | varchar | 255 |  | √ | ' ' |  |
| 3 | fentitycondid | fentitycondid | varchar | 255 |  | √ | 0 |  |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fcontrolrangetwo | fcontrolrangetwo | bpchar | 1 |  | √ | '0' |  |
| 6 | fisunlimited | fisunlimited | bpchar | 1 |  | √ | '0' |  |
| 7 | fcontrolrangefour | fcontrolrangefour | bpchar | 1 |  | √ | '0' |  |
| 8 | fcontrolrangeone | fcontrolrangeone | bpchar | 1 |  | √ | '0' |  |
| 9 | fentitycondset | fentitycondset | varchar | 1000 |  | √ | ' ' |  |
| 10 | fismulti | fismulti | bpchar | 1 |  | √ | '0' |  |
| 11 | fentitycondfilter_tag | fentitycondfilter_tag | text | 0 |  |  | '' |  |
| 12 | fentitycondaligndesc | fentitycondaligndesc | varchar | 50 |  | √ | ' ' |  |
| 13 | fcontrolrangethree | fcontrolrangethree | bpchar | 1 |  | √ | '0' |  |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fentitycondalign | fentitycondalign | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_filter |  | fentryid |
| 2 | idx_msplan_filter_fid |  | fid |
| 3 | idx_msplan_filter_fseq |  | fseq |
