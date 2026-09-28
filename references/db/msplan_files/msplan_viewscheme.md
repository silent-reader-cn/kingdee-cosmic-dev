# 样式方案-msplan_viewscheme

## 每年节假日-子表 t_msplan_holiday

- **表名称：** 每年节假日-子表
- **表名：** t_msplan_holiday

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffestivalname | 节假日名称 | varchar | 50 |  | √ | ' ' | 节假日名称 |
| 3 | fenddaterange | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fstartdaterange | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ffcolorvalue | 颜色值 | varchar | 50 |  | √ | ' ' | 颜色值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_holiday |  | fid,fseq |
| 2 | pk_t_msplan_holiday |  | fentryid |

---

## 数据日期线设置-子表 t_msplan_dataline

- **表名称：** 数据日期线设置-子表
- **表名：** t_msplan_dataline

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatalinetype | 数据日期线类型 | varchar | 5 |  | √ | ' ' | 数据日期线类型,枚举: 0 :计划排程线 1 :日线 3 :月线 2 :年线 4 :周线 |
| 3 | flinecolor | 颜色 | varchar | 50 |  | √ | ' ' | 颜色 |
| 4 | fisshowcurrent | 是否当前显示 | bpchar | 1 |  | √ | '0' | 是否当前显示 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | flinecolorvalue | 颜色值 | varchar | 50 |  | √ | ' ' | 颜色值 |
| 8 | flineshape | 线条类型 | varchar | 5 |  | √ | ' ' | 线条类型,枚举: 1 :实线 2 :虚线 3 :实线加粗 4 :虚线加粗 |
| 9 | fisshow | 是否显示 | bpchar | 1 |  | √ | '0' | 是否显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msplan_dataline |  | fentryid |
| 2 | idx_msplan_dataline |  | fid,fseq |

---

## 横道选项-子表 t_msplan_jvwschcross

- **表名称：** 横道选项-子表
- **表名：** t_msplan_jvwschcross

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcrosstypeid | 横道类型 | int8 | 64 |  | √ | 0 | 横道类型 msplan_gantt_crosstype |
| 3 | fcrossshap | 形状 | varchar | 5 |  | √ | ' ' | 形状,枚举: 1 :圆形 2 :菱形 3 :长方形 |
| 4 | flimitvalue | 限制字符 | int4 | 32 |  | √ | 0 | 限制字符 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fheight | 高度 | varchar | 5 |  | √ | ' ' | 高度,枚举: 20 :20 16 :16 12 :12 8 :8 4 :4 : |
| 7 | fposition | 位置 | varchar | 5 |  | √ | ' ' | 位置,枚举: 1 :居右 2 :居中 3 :居左 |
| 8 | fisline | 是否连线 | bpchar | 1 |  | √ | '0' | 是否连线 |
| 9 | fcrosscolor | 颜色值 | varchar | 50 |  | √ | ' ' | 颜色值 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | flabelisshow | 标签展示 | bpchar | 1 |  | √ | '0' | 标签展示 |
| 12 | fcrossobj | 横道对象 | varchar | 5 |  | √ | ' ' | 横道对象,枚举: 1 :任务横道 2 :里程碑横道 3 :关键路径横道 4 :汇总横道 5 :空闲横道 6 :二级关键路径横道 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_jvwschcross |  | fentryid |
| 2 | idx_msplan_jvwsss_fid |  | fid |
| 3 | idx_msplan_jvwsss_fseq |  | fseq |

---

## 分组字段-子表 t_msplan_jvwschgroup

- **表名称：** 分组字段-子表
- **表名：** t_msplan_jvwschgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityflagid | 实体标识 | varchar | 255 |  | √ | 0 | 主实体对象 bos_entityobject |
| 3 | fgroupflag | 分组字段标志 | varchar | 50 |  | √ | ' ' | 分组字段标志 |
| 4 | fbandcolorval | 分组带颜色值 | varchar | 50 |  | √ | ' ' | 分组带颜色值 |
| 5 | fbandcolor | 分组带颜色 | varchar | 50 |  | √ | ' ' | 分组带颜色 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fgrouplevel | 到层次 | int4 | 32 |  | √ | 0 | 到层次 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_jvwsup_fid |  | fid |
| 2 | pk_msplan_jvwschgroup |  | fentryid |
| 3 | idx_msplan_jvwsup_fseq |  | fseq |

---

## 样式方案-多语言表 t_msplan_vwscheme_l

- **表名称：** 样式方案-多语言表
- **表名：** t_msplan_vwscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 样式名称 | varchar | 100 |  | √ | ' ' | 样式名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_vwscheme_l |  | fpkid |
| 2 | idx_msplan_vwscmel_fname |  | fname |
| 3 | idx_msplan_vwscmel_fid |  | fid,flocaleid |

---

## 字段设置-子表 t_msplan_jvwschemset

- **表名称：** 字段设置-子表
- **表名：** t_msplan_jvwschemset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcolumnflag | 字段列 | varchar | 5 |  | √ | ' ' | 字段列,枚举: A :第一列 B :第二列 C :第三列 D :第四列 E :第五列 F :第六列 G :第七列 |
| 3 | falign | 对齐方式 | varchar | 10 |  | √ | ' ' | 对齐方式,枚举: left :左对齐 right :右对齐 center :居中 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcolwidth | 列宽(px) | numeric | 23 | 10 | √ | 0 | 列宽(px) |
| 6 | ffontsize | 字体大小(px) | numeric | 23 | 10 | √ | 0 | 字体大小(px) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_jvwschemset |  | fentryid |
| 2 | idx_msplan_jvwset_fid |  | fid |
| 3 | idx_msplan_jvwset_fseq |  | fseq |

---

## 样式方案-主表 t_msplan_vwscheme

- **表名称：** 样式方案-主表
- **表名：** t_msplan_vwscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fshowlvlline | 显示水平线 | bpchar | 1 |  | √ | '0' | 显示水平线 |
| 3 | ffirstym | 年度+月 | bpchar | 1 |  | √ | '0' | 年度+月 |
| 4 | ffriday | 星期五 | bpchar | 1 |  | √ | '0' | 星期五 |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | ffirstyear | 年度 | bpchar | 1 |  | √ | '0' | 年度 |
| 7 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | ftuesday | 星期二 | bpchar | 1 |  | √ | '0' | 星期二 |
| 11 | fsecondhour | 时 | bpchar | 1 |  | √ | '0' | 时 |
| 12 | fshowhline | 显示垂直线 | bpchar | 1 |  | √ | '0' | 显示垂直线 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | finternalrow | 间隔行 | int4 | 32 |  | √ | 0 | 间隔行 |
| 16 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 17 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 18 | fsaturday | 星期六 | bpchar | 1 |  | √ | '0' | 星期六 |
| 19 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fassislinetype | 线形 | varchar | 5 |  | √ | ' ' | 线形,枚举: 1 :实线 2 :虚线 |
| 22 | fname | 样式名称 | varchar | 100 |  | √ | ' ' | 样式名称 |
| 23 | fwednesday | 星期三 | bpchar | 1 |  | √ | '0' | 星期三 |
| 24 | fsecondyear | 月 | bpchar | 1 |  | √ | '0' | 月 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fsunday | 星期天 | bpchar | 1 |  | √ | '0' | 星期天 |
| 27 | fcolorvalue | 颜色值 | varchar | 50 |  | √ | ' ' | 颜色值 |
| 28 | fsecondym | 天 | bpchar | 1 |  | √ | '0' | 天 |
| 29 | fassishlinetype | 线形 | varchar | 5 |  | √ | ' ' | 线形,枚举: 1 :实线 2 :虚线 |
| 30 | fctrlstrategy | fctrlstrategy | varchar | 5 |  | √ | ' ' |  |
| 31 | fshowdatal | 显示数据日期线 | bpchar | 1 |  | √ | '0' | 显示数据日期线 |
| 32 | fsecondyq | 周 | bpchar | 1 |  | √ | '0' | 周 |
| 33 | fissys | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 34 | fplanarea | 计划区 | bpchar | 1 |  | √ | '0' | 计划区 |
| 35 | ftodoarea | 待排区 | bpchar | 1 |  | √ | '0' | 待排区 |
| 36 | fthursday | 星期四 | bpchar | 1 |  | √ | '0' | 星期四 |
| 37 | farea | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 38 | flinetype | 线形 | varchar | 5 |  | √ | ' ' | 线形,枚举: 1 :实线 2 :虚线 |
| 39 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 40 | fsummaryarea | 统计区 | bpchar | 1 |  | √ | '0' | 统计区 |
| 41 | fnumber | 样式编码 | varchar | 30 |  | √ | ' ' | 样式编码 |
| 42 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 43 | finternalcol | 间隔列 | int4 | 32 |  | √ | 0 | 间隔列 |
| 44 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 45 | fmonday | 星期一 | bpchar | 1 |  | √ | '0' | 星期一 |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | ffirstyq | 年度+月+日 | bpchar | 1 |  | √ | '0' | 年度+月+日 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_vwscheme |  | fid |
| 2 | idx_msplan_vwscme_fnumber |  | fnumber |
| 3 | idx_msplan_vwscme_fcreatetime |  | fcreatetime |
