# 工卡历史快照-mpdm_mrocardroute_h

## 页面工时信息-子表 t_mpdm_processversion_h

- **表名称：** 页面工时信息-子表
- **表名：** t_mpdm_processversion_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fname | 工卡号 | varchar | 255 |  | √ | ' ' | 工卡号 |
| 5 | fhouroriginalid | 原始id | int8 | 64 |  | √ | 0 | 原始id |
| 6 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 |
| 11 | fcalsumhours | 消耗总工时（计算） | numeric | 23 | 10 | √ | 0 | 消耗总工时（计算） |
| 12 | fpagesumhours | 页面总工时（小时） | numeric | 23 | 10 | √ | 0 | 页面总工时（小时） |
| 13 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | fsalehours | 售卖工时(小时） | numeric | 23 | 10 | √ | 0 | 售卖工时(小时） |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 页码 | varchar | 50 |  | √ | ' ' | 页码 |
| 17 | fexpirationdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 18 | fcustomesumhours | 消耗总工时（小时） | numeric | 23 | 10 | √ | 0 | 消耗总工时（小时） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_processversion_h_fk |  | fcardid |
| 2 | pk_mpdm_processversion_h |  | fid |

---

## 工序序列-子表 t_mpdm_wkentryseq_h

- **表名称：** 工序序列-子表
- **表名：** t_mpdm_wkentryseq_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 检修工艺序列FID | int8 | 64 |  | √ | 0 | 检修工艺序列FID |
| 2 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 3 | fprocessseqtype | 序列类型 | varchar | 50 |  | √ | ' ' | 序列类型,枚举: A :主序列 B :并行序列 C :替代序列 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fversionid | 版本id | int8 | 64 |  | √ | 0 | 版本id |
| 6 | foutput | 转出工序 | varchar | 50 |  | √ | ' ' | 转出工序 |
| 7 | fprocessseqremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | finput | 转入工序 | varchar | 50 |  | √ | ' ' | 转入工序 |
| 9 | fprocessseqname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |
| 10 | frelation | 并行关系 | varchar | 50 |  | √ | ' ' | 并行关系,枚举: A :开始-开始 B :开始-结束 C :结束-开始 D :结束-结束 |
| 11 | freference | 参照序列 | varchar | 50 |  | √ | ' ' | 参照序列 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fprocessseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 14 | fseqoriginalid | 原始id | int8 | 64 |  | √ | 0 | 原始id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_wkentryseq_h |  | fentryid |
| 2 | idx_mpdm_wkentryseq_h_fk |  | fcardid |

---

## 功能位置-多选基础资料表 t_mpdm_mrowkzone_h

- **表名称：** 功能位置-多选基础资料表
- **表名：** t_mpdm_mrowkzone_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [功能位置 mpdm_functionlocation](../mpdm_files/mpdm_functionlocation.md) |
| 2 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_mrowkzone_h |  | fpkid |
| 2 | idx_mpdm_mrowneh_fcardid |  | fcardid,fbasedataid |

---

## 序列关系-子表 t_mpdm_wkentryseqrel_h

- **表名称：** 序列关系-子表
- **表名：** t_mpdm_wkentryseqrel_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 检修工艺关系FID | int8 | 64 |  | √ | 0 | 检修工艺关系FID |
| 2 | ftransferprocessname | 转入工序名称 | varchar | 50 |  | √ | ' ' | 转入工序名称 |
| 3 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 4 | fseqrelationname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fturnoutprocessname | 转出工序名称 | varchar | 50 |  | √ | ' ' | 转出工序名称 |
| 7 | fseqrelationparseq | 并行序列号 | varchar | 50 |  | √ | ' ' | 并行序列号 |
| 8 | fseqrelationparname | 并行序列名称 | varchar | 50 |  | √ | ' ' | 并行序列名称 |
| 9 | ftransferprocessno | 转入工序号 | varchar | 50 |  | √ | ' ' | 转入工序号 |
| 10 | fseqrelationseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 11 | fparallelration | 并行关系 | varchar | 50 |  | √ | ' ' | 并行关系,枚举: A :开始-开始 B :结束-开始 C :结束-结束 D :开始-结束 |
| 12 | fturnoutprocessno | 转出工序号 | varchar | 50 |  | √ | ' ' | 转出工序号 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | freloriginalid | 原始id | int8 | 64 |  | √ | 0 | 原始id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_wkentryseqrel_h |  | fentryid |
| 2 | idx_mpdm_wkentryseqrel_h_fk |  | fcardid |

---

## 子单据体-子表 t_mpdm_subentryroute_h

- **表名称：** 子单据体-子表
- **表名：** t_mpdm_subentryroute_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fresourceid | 资源编码 | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fsourceoriginalid | 原始id | int8 | 64 |  | √ | 0 | 原始id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_subentryroute_h |  | fdetailid |
| 2 | idx_mpdm_subentryroute_h_fk |  | fentryid |

---

## 文件信息-子表 t_mpdm_wkentrydoc_h

- **表名称：** 文件信息-子表
- **表名：** t_mpdm_wkentrydoc_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdocsecltion | 章 | varchar | 50 |  | √ | ' ' | 章 |
| 2 | fdocoriginalid | 原始id | int8 | 64 |  | √ | 0 | 原始id |
| 3 | fdocversion | 文档版本 | varchar | 50 |  | √ | ' ' | 文档版本 |
| 4 | fdocparagraph | 段 | varchar | 50 |  | √ | ' ' | 段 |
| 5 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 6 | fdoctype | 文档类型 | int8 | 64 |  | √ | 0 | [文件类型 mpdm_doctype](../mpdm_files/mpdm_doctype.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fdocpart | 节 | varchar | 50 |  | √ | ' ' | 节 |
| 10 | fdocnum | 文档编号 | varchar | 50 |  | √ | ' ' | 文档编号 |
| 11 | fdocpagenum | 页 | varchar | 50 |  | √ | ' ' | 页 |
| 12 | ftextfield | 描述 | varchar | 50 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_wkentrydoc_h |  | fentryid |
| 2 | idx_mpdm_wkentrydoc_h_fk |  | fcardid |

---

## 页面工时信息-多语言表 t_mpdm_processversion_h_l

- **表名称：** 页面工时信息-多语言表
- **表名：** t_mpdm_processversion_h_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工卡号 | varchar | 255 |  | √ | ' ' | 工卡号 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_processversion_h_l |  | fpkid |
| 2 | idx_mpdm_processversion_h_l_0 |  | fid,flocaleid |

---

## 工序活动-子表 t_mpdm_wkactivity_h

- **表名称：** 工序活动-子表
- **表名：** t_mpdm_wkactivity_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | factscheduling | 排程 | bpchar | 1 |  | √ | '1' | 排程 |
| 2 | fstandardformula1id | 标准公式 | int8 | 64 |  | √ | 0 | [工序活动公式(废弃) mpdm_processformula](../mpdm_files/mpdm_processformula.md) |
| 3 | fprocessno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | foperationnumber | 工序名称 | varchar | 50 |  | √ | ' ' | 工序名称 |
| 6 | factivityid | 活动编码 | int8 | 64 |  | √ | 0 | [工序活动定义(废弃) mpdm_processactivity](../mpdm_files/mpdm_processactivity.md) |
| 7 | fprocessstage | 工序阶段 | varchar | 50 |  | √ | ' ' | 工序阶段,枚举: A :排队阶段 B :准备阶段 C :加工阶段 D :拆卸阶段 E :等待阶段 F :转移阶段 |
| 8 | fminformulaid | 最小值公式 | int8 | 64 |  | √ | 0 | [工序活动公式(废弃) mpdm_processformula](../mpdm_files/mpdm_processformula.md) |
| 9 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: A :生产 B :成本 C :工资 |
| 10 | fstandardformulaid | 标准公式 | int8 | 64 |  | √ | 0 | [工序活动公式(废弃) mpdm_processformula](../mpdm_files/mpdm_processformula.md) |
| 11 | factresourceid | 资源 | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 12 | factoriginalid | 原始id | int8 | 64 |  | √ | 0 | 原始id |
| 13 | fminformula1id | 最小值公式 | int8 | 64 |  | √ | 0 | [工序活动公式(废弃) mpdm_processformula](../mpdm_files/mpdm_processformula.md) |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 15 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_wkactivity_h_fk |  | fentryid |
| 2 | pk_mpdm_wkactivity_h |  | fdetailid |

---

## 工作区域-多选基础资料表 t_mpdm_mrowkarea_h

- **表名称：** 工作区域-多选基础资料表
- **表名：** t_mpdm_mrowkarea_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [工作区域 mpdm_area](../mpdm_files/mpdm_area.md) |
| 2 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_mroweah_fcardid |  | fcardid,fbasedataid |
| 2 | pk_mpdm_mrowkarea_h |  | fpkid |

---

## 工序信息-子表 t_mpdm_mentryroute_h

- **表名称：** 工序信息-子表
- **表名：** t_mpdm_mentryroute_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 检修工艺工序FID | int8 | 64 |  | √ | 0 | 检修工艺工序FID |
| 2 | fproductionworkshopid | 生产车间 | int8 | 64 |  | √ | 0 | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 3 | ffirstcheck | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 4 | ftaxrate | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | foperationqty | 工序数量 | numeric | 23 | 10 | √ | 0 | 工序数量 |
| 7 | fchecktype | 检验方式 | varchar | 50 |  | √ | ' ' | 检验方式,枚举: 1011 :免检 1012 :车间检验 1013 :质量检验 |
| 8 | fbasebatchqty | 基本批量 | numeric | 23 | 10 | √ | 0 | 基本批量 |
| 9 | foperationid | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 10 | fprocessgroup | 工序组 | int8 | 64 |  | √ | 0 | [工序组(废弃) mpdm_progroup](../mpdm_files/mpdm_progroup.md) |
| 11 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 12 | fversionid | 版本id | int8 | 64 |  | √ | 0 | 版本id |
| 13 | fpageseq1 | 页码 | varchar | 50 |  | √ | ' ' | 页码 |
| 14 | fsplitqty | 建议拆分数 | numeric | 23 | 10 | √ | 0 | 建议拆分数 |
| 15 | foperationunitid | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 18 | fheadqty | 表头数量 | numeric | 23 | 10 | √ | 0 | 表头数量 |
| 19 | fworkstation | 工位 | int8 | 64 |  | √ | 0 | [工位 mpdm_workstation](../mpdm_files/mpdm_workstation.md) |
| 20 | foperationdesc | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 21 | foverlaptimeunit | 重叠时间单位 | varchar | 50 |  | √ | ' ' | 重叠时间单位,枚举: A :分钟 B :秒 |
| 22 | ftimeunit | 加工时间单位 | varchar | 50 |  | √ | ' ' | 加工时间单位,枚举: A :分钟 B :秒 |
| 23 | fisprocessoverlap | 是否工序重叠 | bpchar | 1 |  | √ | '0' | 是否工序重叠 |
| 24 | fprofessiona | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 25 | fcurrencyfield | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | foperationno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 28 | foverlapqty | 重叠批量 | numeric | 23 | 10 | √ | 0 | 重叠批量 |
| 29 | fpurchasegroupid | 采购组 | int8 | 64 |  | √ | 0 | [采购业务组(封存) bd_pmoperatorgroup](../sbd_files/bd_pmoperatorgroup.md) |
| 30 | fcustomhours | 消耗工时（小时） | numeric | 23 | 10 | √ | 0 | 消耗工时（小时） |
| 31 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 32 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 33 | fmachiningtype | 加工类型 | varchar | 50 |  | √ | ' ' | 加工类型,枚举: 1001 :厂内加工 1002 :委外加工 1003 :内协加工 1004 :不限制 |
| 34 | foverlapunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | ffloorratio | 汇报下限比例(%) | numeric | 23 | 10 | √ | 0 | 汇报下限比例(%) |
| 36 | fentrymaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 37 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 38 | fminoverlaptime | 重叠最小时间 | numeric | 23 | 10 | √ | 0 | 重叠最小时间 |
| 39 | fstandardhours | 标准工时（小时） | numeric | 23 | 10 | √ | 0 | 标准工时（小时） |
| 40 | fminworktime | 最小加工时间 | numeric | 23 | 10 | √ | 0 | 最小加工时间 |
| 41 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 42 | fparentid | 工序序列 | varchar | 50 |  | √ | ' ' | 工序序列 |
| 43 | fsettlementcoefficient | 结算系数 | numeric | 23 | 10 | √ | 0 | 结算系数 |
| 44 | fissplit | 是否拆分排程 | bpchar | 1 |  | √ | '0' | 是否拆分排程 |
| 45 | fpurchasepersonid | 采购员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | foprctrlstrategy | 工序控制策略 | int8 | 64 |  | √ | 0 | [工序控制策略(废弃) mpdm_proctrlstrategy](../mpdm_files/mpdm_proctrlstrategy.md) |
| 47 | fbottleprocedure | 瓶颈工序 | bpchar | 1 |  | √ | '0' | 瓶颈工序 |
| 48 | fprocessoriginalid | 原始id | int8 | 64 |  | √ | 0 | 原始id |
| 49 | fproductionorgid | 加工组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 50 | fheadunitid | 表头单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 51 | fupperratio | 汇报上限比例(%) | numeric | 23 | 10 | √ | 0 | 汇报上限比例(%) |
| 52 | fismilestoneprocess | 里程碑工序 | bpchar | 1 |  | √ | '0' | 里程碑工序 |
| 53 | fcollaborative | 协作工序 | bpchar | 1 |  | √ | '0' | 协作工序 |
| 54 | fsettlementunitid | 结算单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_mentryroute_h_fk |  | fcardid |
| 2 | pk_mpdm_mentryroute_h |  | fentryid |

---

## 附件-附件表 t_mpdm_wkdocatta_h

- **表名称：** 附件-附件表
- **表名：** t_mpdm_wkdocatta_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_wkdocatta_h |  | fpkid |
| 2 | idx_mpdm_wkdocatta_h_fk |  | fentryid |

---

## 面板信息-子表 t_mpdm_wkentrypanel_h

- **表名称：** 面板信息-子表
- **表名：** t_mpdm_wkentrypanel_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpanelnumber | 面板编码 | int8 | 64 |  | √ | 0 | [面板定义 mpdm_paneldef](../mpdm_files/mpdm_paneldef.md) |
| 2 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 3 | fpaneloriginalid | 原始id | int8 | 64 |  | √ | 0 | 原始id |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fpanelsumhours | 面板拆装工时（小时） | numeric | 23 | 10 | √ | 0 | 面板拆装工时（小时） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_wkentrypanel_h |  | fentryid |
| 2 | idx_mpdm_wkentrypanel_h_fk |  | fcardid |

---

## 工卡历史快照-主表 t_mpdm_mrocardroute_h

- **表名称：** 工卡历史快照-主表
- **表名：** t_mpdm_mrocardroute_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid主键 | int8 | 64 |  | √ | 0 | fid主键 |
| 2 | fgroupid | 工作类别 | int8 | 64 |  | √ | 0 | [工作类别 mpdm_workcategories](../mpdm_files/mpdm_workcategories.md) |
| 3 | fladder | 需要梯架 | bpchar | 1 |  | √ | '0' | 需要梯架 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fphotoversion | 快照版本 | varchar | 50 |  | √ | ' ' | 快照版本 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | friskcard | 风险卡 | bpchar | 1 |  | √ | '0' | 风险卡 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fworkcardtype | 工卡类型 | int8 | 64 |  | √ | 0 | [工卡类型 mpdm_jobcardtype](../mpdm_files/mpdm_jobcardtype.md) |
| 10 | fcardnumid | 工卡辅助识别码 | varchar | 80 |  | √ | ' ' | 工卡辅助识别码 |
| 11 | froutereplace | 替代号 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_routereplace](../mpdm_files/mpdm_routereplace.md) |
| 12 | fcanceltime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 13 | frefwordcard | 参考工卡编码 | int8 | 64 |  | √ | 0 | [维修计划工卡 mpdm_maintenanceplan](../mpdm_files/mpdm_maintenanceplan.md) |
| 14 | fmajorflag | 重要工作标记 | bpchar | 1 |  | √ | '0' | 重要工作标记 |
| 15 | fproductenvironment | 生产环境 | varchar | 255 |  | √ | ' ' | 生产环境 |
| 16 | fbaseata | 章节号 | int8 | 64 |  | √ | 0 | [ATA章节号 mpdm_atachapterno](../mpdm_files/mpdm_atachapterno.md) |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fsumhours | 总工时（小时） | numeric | 23 | 10 | √ | 0 | 总工时（小时） |
| 19 | fworkunit | 工时单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fname | 标题 | varchar | 255 |  | √ | ' ' | 标题 |
| 21 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 22 | fmuldescribe | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fcardid | fcardid | int8 | 64 |  | √ | 0 | id |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fversionid | 版本 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_processversion](../mpdm_files/mpdm_processversion.md) |
| 26 | fconditiionexe | 执行条件（封存） | int8 | 64 |  | √ | 0 | [执行条件 mpdm_execondition](../mpdm_files/mpdm_execondition.md) |
| 27 | ffirstexe | 首次执行 | bpchar | 1 |  | √ | '1' | 首次执行 |
| 28 | fpanel | 需要面板 | bpchar | 1 |  | √ | '0' | 需要面板 |
| 29 | fmulfremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 30 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 32 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fzone | 主功能位置 | int8 | 64 |  | √ | 0 | [功能位置 mpdm_functionlocation](../mpdm_files/mpdm_functionlocation.md) |
| 35 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 36 | fdescribe | 备注（封存） | varchar | 255 |  | √ | ' ' | 备注（封存） |
| 37 | fcardspecial | 特殊工卡标识 | varchar | 255 |  | √ | ' ' | 特殊工卡标识 |
| 38 | fmaterialgroupid | 物料控制组 | int8 | 64 |  | √ | 0 | [物料控制组 bd_materialcontrolgroup](../basedata_files/bd_materialcontrolgroup.md) |
| 39 | fata | 章节号(废弃) | varchar | 50 |  | √ | ' ' | 章节号(废弃) |
| 40 | fmajordesc | 重要工作描述（封存） | varchar | 255 |  | √ | ' ' | 重要工作描述（封存） |
| 41 | friskref | 风险信息 | int8 | 64 |  | √ | 0 | [风险定义 mpdm_riskdef](../mpdm_files/mpdm_riskdef.md) |
| 42 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 43 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 44 | fcancelerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcardversion | 客户工卡版本号 | varchar | 50 |  | √ | ' ' | 客户工卡版本号 |
| 46 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 48 | fmoddate | 修订日期 | timestamp | 0 |  |  | null | 修订日期 |
| 49 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 50 | fmaintrade | 主行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 51 | fcardintegrity | 工卡完整性 | varchar | 50 |  | √ | ' ' | 工卡完整性,枚举: A :未完成 B :部分完成 C :已完成 |
| 52 | fworkarea | 主工作区域 | int8 | 64 |  | √ | 0 | [工作区域 mpdm_area](../mpdm_files/mpdm_area.md) |
| 53 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fbomversionid | BOM | int8 | 64 |  | √ | 0 | BOM模板 mpdm_bomtpl |
| 55 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 56 | fremark | 备注（封存） | varchar | 255 |  | √ | ' ' | 备注（封存） |
| 57 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 58 | fcardhourtype | 工时类型 | varchar | 50 |  | √ | ' ' | 工时类型,枚举: A :拆卸 B :安装 |
| 59 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 60 | fexepriority | 执行优先级 | int8 | 64 |  | √ | 0 | 执行优先级 |
| 61 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 62 | fspecialcustom | 特殊客户标识（封存） | bpchar | 1 |  | √ | '0' | 特殊客户标识（封存） |
| 63 | fprocesstype | 工艺类型 | varchar | 50 |  | √ | ' ' | 工艺类型,枚举: A :物料 B :物料组 C :通用 D :检修设备类型 E :例行 |
| 64 | fcardnum | 客户工卡号 | varchar | 80 |  | √ | ' ' | 客户工卡号 |
| 65 | fmaterialtype | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 66 | fmulmajordesc | 重要工作描述 | varchar | 255 |  | √ | ' ' | 重要工作描述 |
| 67 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 68 | fneedmaterial | 需要物料 | varchar | 50 |  | √ | ' ' | 需要物料,枚举: A :待确认 B :需要 C :不需要 |
| 69 | fbusinesscontrol | 业务控制 | varchar | 255 |  | √ | ' ' | 业务控制 |
| 70 | fismainprocess | 主工艺路线 | bpchar | 1 |  | √ | '1' | 主工艺路线 |
| 71 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 72 | fcardid2 | 工卡id | int8 | 64 |  | √ | 0 | 工卡id |
| 73 | fneedtool | 需要工具 | varchar | 50 |  | √ | ' ' | 需要工具,枚举: A :待确认 B :需要 C :不需要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fcardid | fcardid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_mrocardr_h_cid2 |  | fcardid2 |
| 2 | idx_t_mpdm_mrocardr_h_master |  | fmasterid |
| 3 | idx_t_mpdm_mrocardroute_h_cg |  | fcreateorgid |
| 4 | idx_t_mpdm_mrocardroute_h_master |  | fmasterid |
| 5 | idx_t_mpdm_mrocardroute_h_createorg |  | fcreateorgid |
| 6 | pk_mpdm_mrocardroute_h |  | fcardid |

---

## 重要工作描述涉及行业-多选基础资料表 t_mpdm_mrotraderelation_h

- **表名称：** 重要工作描述涉及行业-多选基础资料表
- **表名：** t_mpdm_mrotraderelation_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 2 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_mrotraderelation_h |  | fpkid |
| 2 | idx_mpdm_mrotraderelation_h_fk |  | fcardid |

---

## 工卡历史快照-使用范围表 t_mpdm_mrocardroute_h_u

- **表名称：** 工卡历史快照-使用范围表
- **表名：** t_mpdm_mrocardroute_h_u

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
| 1 | idx_t_mpdm_mrocardroute_h_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_mrocardroute_h_u |  | fdataid,fuseorgid |

---

## 工卡历史快照-多语言表 t_mpdm_mrocardroute_h_l

- **表名称：** 工卡历史快照-多语言表
- **表名：** t_mpdm_mrocardroute_h_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 标题 | varchar | 255 |  | √ | ' ' | 标题 |
| 3 | fmuldescribe | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 5 | fmulfremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 8 | fmulmajordesc | 重要工作描述 | varchar | 255 |  | √ | ' ' | 重要工作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_mrocardroute_h_l_0 |  | fcardid,flocaleid |
| 2 | pk_mpdm_mrocardroute_h_l |  | fpkid |

---

## 类型标识-多选基础资料表 t_mpdm_mrowkidentity_h

- **表名称：** 类型标识-多选基础资料表
- **表名：** t_mpdm_mrowkidentity_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [类型标识 mpdm_typeidentity](../mpdm_files/mpdm_typeidentity.md) |
| 2 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_mrowkidentity_h_fk |  | fcardid |
| 2 | pk_mpdm_mrowkidentity_h |  | fpkid |

---

## 执行条件-多选基础资料表 t_mpdm_mulconexe_h

- **表名称：** 执行条件-多选基础资料表
- **表名：** t_mpdm_mulconexe_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [执行条件 mpdm_execondition](../mpdm_files/mpdm_execondition.md) |
| 2 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_mulconexe_h |  | fpkid |
| 2 | idx_mpdm_mulconexe_h_fk |  | fcardid |
